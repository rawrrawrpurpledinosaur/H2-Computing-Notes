from pymongo import MongoClient
import json

# Connect to the database
client = pymongo.MongoClient("localhost", 27017)

db = client["travel"]

collection = db["flights"]

# Insert documents into db
with open("flights.json", "r") as file:
    data = json.load(file)
    collection.insert_many(data)

# Print all documents in the "customers" collection
for x in collection.find():
    print(x)

# Updating "price" field to be 90% for everyone
collection.update_many({}, {"$mul": {"price": 0.9}})
for x in collection.find():
    print(x)

# Display city and price for flights less than 10 hours and $300
for x in collection.find({"duration": {"$lt": 10}, "price": {"$lt": 300}}, {"city": 1, "price": 1}):
    print(x)
