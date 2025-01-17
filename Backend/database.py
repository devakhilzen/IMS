from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
MONGO_COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME")
MONGO_COLLECTION_NAME_TWO = os.getenv("MONGO_COLLECTION_NAME_TWO")
MONGO_COLLECTION_NAME_THREE = os.getenv("MONGO_COLLECTION_NAME_THREE")

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB_NAME]
items_collection = db[MONGO_COLLECTION_NAME]
users_collection = db[MONGO_COLLECTION_NAME_TWO]
transactions_collection = db[MONGO_COLLECTION_NAME_THREE]