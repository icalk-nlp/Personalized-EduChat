from typing import Callable, Union, List
import weaviate
from weaviate.util import generate_uuid5

from config import Config
from document_store.base_store import BaseStore
from document_store.document import Document
from utils.embedding import get_embedding
from utils.weaviate import get_client
from utils.weaviate.weaviate_utils import query_from_weavite


class object(dict):
    document: str
    metadata: str


class WeaviateStore(BaseStore):
    _url: str
    _class_name: str
    _vectorize_method: Callable
    _max_length: int
    _limit: int

    def __init__(self, class_name, **kwargs):
        super().__init__(**kwargs)
        self._url = Config().get("WEAVIATE_URL")
        self._client = get_client(self._url)
        self._class_name = class_name
        self._max_length = kwargs.get("max_length", 256)
        self._limit = kwargs.get("limit", 3)

    def search(self, query, limit=3, **kwargs) -> str:
        contents = self._query_weaviate_database(self._class_name, query, limit, **kwargs)
        return contents

    def _query_weaviate_database(self, class_name, query, limit=3, where_filter=None, sort=None) -> str:
        query_vector = get_embedding().embed_query(query)
        near_vector = {"vector": query_vector}
        response = query_from_weavite(self._url, class_name, ["document", "metadata"], near_vector=near_vector,
                                      limit=limit, where_filter=where_filter, sort=sort)
        contents = []
        for r in response:
            content = ""
            for p in ["document", "metadata"]:
                content += f"{p}:{r[p]}\n"
            contents.append(content)
            return "\n".join(contents)

    def persist(self):
        raise NotImplementedError

    def add(self, data_object: dict):
        content = data_object["document"]
        uuid = self._client.data_object.create(
            data_object=data_object,
            class_name=self._class_name,
            vector=get_embedding().embed_query(content),
            uuid=generate_uuid5(data_object)
        )
        return uuid

    # Write document to the database
    def write(self, document: Document):
        docs, metadatas = document.get_docs_and_metadatas()
        objects = []
        for doc, meta in zip(docs, metadatas):
            obj = {
                "document": doc,
                "metadata": meta
            }
            objects.append(obj)
        vectors = get_embedding().embed_docs(docs)
        with self._client.batch(batch_size=100, dynamic=True) as batch:
            for i, data_obj in enumerate(objects):
                batch.add_data_object(
                    data_obj,
                    class_name=self._class_name,
                    vector=vectors[i],
                    uuid=generate_uuid5(data_obj)
                )

    # Delete a class
    def delete(self):
        self._client.schema.delete_class(class_name=self._class_name)


if __name__ == '__main__':
    store = WeaviateStore(class_name="Menu")
    one_object = object(document="白菜", metadata="2.5元/斤")
    print(one_object)
    one_id = store.add(one_object)
    print(one_id)
    print(store.search(query="白菜"))
