from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from mongoengine import connect

from config import settings


uri = f"mongodb+srv://{settings.USERNAME_MONGO}:{settings.PASSWORD_MONGO}@{settings.CLUSTER_MONGO}.hmksneo.mongodb.net/somedb?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

db = client.book

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


connect(host=uri)
