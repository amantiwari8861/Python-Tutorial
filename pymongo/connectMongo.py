from pymongo import MongoClient

client = MongoClient("mongodb+srv://root:1234@mongocluster.hw6ib.mongodb.net/?retryWrites=true&w=majority&appName=MongoCluster")
db = client["ecommerce"]
collection = db["users"]  # Updated collection name

user=collection.find_one({"userId":101})
print(user)
