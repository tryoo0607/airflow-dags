from elasticsearch import Elasticsearch, helpers


def save_to_elasticsearch(
    items: List[Dict],
    index_name: str,
    es_host: str,
) -> None:
    es = Elasticsearch(es_host)

    actions = [
        {
            "_index": index_name,
            "_id": item["id"],
            "_source": item,
        }
        for item in items
    ]

    helpers.bulk(es, actions)
