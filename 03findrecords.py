import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# result = mycollection.find_one()

for data in mycollection.find({}, {"_id" : 0, "name" : 1, "price" : 1}):
    print(data)

# print(result)