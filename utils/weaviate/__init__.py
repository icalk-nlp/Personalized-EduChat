import os
import atexit

import weaviate
WEAVIATE_CONNECTION_POOL = {

}

def get_client(url):
    if url not in WEAVIATE_CONNECTION_POOL or not WEAVIATE_CONNECTION_POOL[url].is_live():
        WEAVIATE_CONNECTION_POOL[url] = weaviate.Client(url)
    return WEAVIATE_CONNECTION_POOL[url]
