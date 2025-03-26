from pymongo import MongoClient
from app.config import settings

client = None

def connect_db():
    global client
    client = MongoClient(settings.mongodb_uri)
    # Optionally, set up DB indices or collections
    print("Connected to MongoDB")
