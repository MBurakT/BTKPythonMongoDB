import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# mycollection.update_one(
#     {"name" : "Samsung S6"}, 
#     {"$set" : {
#         "name" : "IPhone 7", 
#         "price" : 5000
#     }}
# )

mycollection.update_many(
    {"name" : "Samsung S7"}, 
    {"$set" : {
        "name" : "IPhone 8", 
        "price" : 5000
    }}
)

for data in mycollection.find():
    print(data)