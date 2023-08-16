
from typing import Callable, Union, List
import weaviate

from config import Config
from document_store.base_store import BaseStore
from utils.embedding import get_embedding
from utils.weaviate import get_client
from utils.weaviate.weaviate_utils import query_from_weavite


class WeaviateStore(BaseStore):
    _url: str
    _class_name: str
    _property: Union[str, list[str]]
    _vectorize_method: Callable
    _max_length: int
    _limit: int

    def __init__(self, class_name, property, **kwargs):
        super().__init__(**kwargs)
        self._url = Config().get("WEAVIATE_URL")
        self._client = get_client(self._url)
        self._class_name = class_name
        self._property = property
        self._max_length = kwargs.get("max_length", 256)
        self._limit = kwargs.get("limit", 3)


    def search(self, query, limit=3, **kwargs) -> str:
        query = kwargs.get("query")
        limit = int(kwargs.get("limit", 3))
        class_name = self._class_name
        property_list = self._property if isinstance(self._property, list) else [self._property]
        contents = self._query_weaviate_database(class_name, property_list, query, limit, **kwargs)
        return contents

    def _query_weaviate_database(self, class_name, property, query, limit=3, where_filter=None, sort=None) -> str:
        query_vector = get_embedding().embed_query(query)
        near_vector = {"vector": query_vector}

        if len(property) == 1:
            response: List[dict] = query_from_weavite(self._url, class_name, property, near_vector=near_vector,
                                                      limit=limit, where_filter=where_filter, sort=sort)
            contents = []
            for r in response:
                contents.append(r[property[0]])
            return "，".join(contents)
        else:
            response: List[dict] = query_from_weavite(self._url, class_name, property, near_vector=near_vector,
                                                      limit=limit, where_filter=where_filter, sort=sort)
            contents = []
            for r in response:
                content = ""
                for p in property:
                    content += p + ":" + str(r[p]) + "\n"
                    contents.append("".join(content))
            return "\n ".join(contents)

    def persist(self):
        raise NotImplementedError

    def write(self, **kwargs):
        pass

    def add(self):
        pass

    def delete(self):
        pass