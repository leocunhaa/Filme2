from pymongo import MongoClient

client = MongoClient()
db_connection = client["empresa"]

collection = db_connection.get_collection("filmes")

proj = {"_id": 0}

search_filter = {"Filme": "VelozesEFuriosos"}
response = collection.find(search_filter, proj)

for registry in response: 
    print(registry)
