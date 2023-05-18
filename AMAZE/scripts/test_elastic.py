from elasticsearch import Elasticsearch

# Instantiate an Elasticsearch client
es = Elasticsearch(["http://localhost:9200"], http_auth=("elastic", "root"))


search_query = {"query": {"match_all": {}}}
response = es.search(index="products_index_elastic", body=search_query, size=10000)
documents = response["hits"]["hits"]
for document in documents:
    print(document["_source"])
print(len(documents))
