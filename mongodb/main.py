import pymongo

# Connect to the database
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a database called "mydatabase"
db = client["mydatabase"]

# Create a collection called "customers"
collection = db["customers"]


