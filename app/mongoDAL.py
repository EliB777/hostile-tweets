from pymongo import MongoClient

client = MongoClient("mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/")
db = client["IranMalDB"]
collection = db["tweets"]

documents = collection.find()


# for doc in documents:
#     print(doc)