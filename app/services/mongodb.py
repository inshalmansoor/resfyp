from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.restaurant_voice_agent

# You can create helper functions to get specific collections
def get_collection(collection_name: str):
    return database.get_collection(collection_name)
