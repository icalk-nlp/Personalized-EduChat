from utils.embedding import get_embedding
from utils.weaviate import get_client


def query_from_weavite(url, class_name, properties,
                       limit=None, near_vector=None, where_filter=None, sort=None, query=None,alpha=0.75):
    client = get_client(url)
    query_content = client.query.get(class_name, properties)
    if where_filter:
        query_content = query_content.with_where(where_filter)
    if near_vector:
        if query:
            query_content = query_content.with_hybrid(
                query=query,
                alpha=alpha,
                vector=near_vector
            )
        else:
            query_content = query_content.with_near_vector(near_vector)
    if sort:
        query_content = query_content.with_sort(sort)
    if limit:
        query_content = query_content.with_limit(limit)

    response = (
        query_content.do()
    )
    return response["data"]["Get"][class_name]
