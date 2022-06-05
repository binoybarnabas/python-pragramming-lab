# importing module
from pymongo import MongoClient

# creation of MongoClient
client=MongoClient()

# Connect with the portnumber and host
client = MongoClient("mongodb+srv://root:root@cluster0.7mrqgec.mongodb.net/?retryWrites=true&w=majority")

db = client.test

# Access database
mydatabase = client["test"]

# Access collection of the database
mycollection=mydatabase["student"]

# dictionary to be added in the database
rec={
"title": "MongoDB and Python",
"description": "MongoDB is no SQL database",

}

# inserting the data in the database
mydatabase.myTable.insert(rec)
