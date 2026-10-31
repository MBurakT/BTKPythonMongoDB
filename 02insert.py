import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# product = {"name" : "Samsung S5", "price" : 2000}

# result = mycollection.insert_one(product)

# print(result)
# print(type(result))
# print(result.inserted_id)

# product_list = [
#     {"_id" : 1, "name" : "Samsung S7", "price" : 4000}, 
#     {"_id" : 2, "name" : "Samsung S8", "price" : 5000}, 
#     {"_id" : 3, "name" : "Samsung S6", "price" : 3000}, 
#     {"_id" : 4, "name" : "Samsung S9", "price" : 6000}, 
#     {"_id" : 5, "name" : "Samsung S10", "price" : 7000}, 
#     {"_id" : 6, "name" : "Samsung S11", "price" : 8000}
# ]

product_list = [
    {"name" : "Samsung S7", "price" : 4000, "description": "iyi telefon"}, 
    {"name" : "Samsung S8", "price" : 5000, "categories" : ['telefon', 'elektronik']}
]

result = mycollection.insert_many(product_list)
print(result.inserted_ids)