import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# result = mycollection.find({"name" : "Samsung S5"})
# result = mycollection.find_one({"_id" : ObjectId("6ae5e4a3a3d9421e0f5ab704")})

# result = mycollection.find({
#     "name" : {
#         "$in" : ["Samsung S5", "Samsung S6"]
#     }
# })

# result = mycollection.find({
#     "price" : {
#         "$gte" : 2000
#     }
# })

# result = mycollection.find({
#     "price" : {
#         "$eq" : 2000
#     }
# })

# result = mycollection.find({
#     "price" : {
#         "$lte" : 2000
#     }
# })

result = mycollection.find({
    "name" : {"$regex" : "^S"}
})

for data in result:
    print(data)

# print(result)