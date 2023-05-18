from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
import os
import json

# Instantiate an Elasticsearch client with authentication credentials
es = Elasticsearch(["http://localhost:9200"], http_auth=("elastic", "root"))


# Define the search query to match all documents
search_query = {"query": {"match_all": {}}}

# Use the Scroll API to retrieve all documents in the index
response = es.search(
    index="products_index_elastic",
    body=search_query,
    scroll="10m",  # Scroll context validity time
    size=1000,  # Number of documents to retrieve per scroll request
)

scroll_id = response["_scroll_id"]
total_documents = response["hits"]["total"]["value"]
processed_documents = 0


# Process the initial batch of documents
for document in response["hits"]["hits"]:
    # print(document["_source"])
    processed_documents += 1

# # Continue scrolling through the remaining documents
# while processed_documents < total_documents:
#     response = es.scroll(scroll_id=scroll_id, scroll="10m")
#     scroll_id = response["_scroll_id"]

#     # Process the next batch of documents
#     for document in response["hits"]["hits"]:
#         print(document["_source"])
#         processed_documents += 1

a = len(response["hits"]["hits"])
print(f"Total documents: {total_documents} \nscroll_id's : {scroll_id},\nresponse: {a}")

with open("data.json","w") as file:
    file.write(json.dumps(response))
