import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# mycollection.delete_one({"name" : "Samsung S5"})

mycollection.delete_many({"name" : {"$regex" : "^S"}})

for data in mycollection.find():
    print(data)