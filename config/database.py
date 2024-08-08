from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
password = os.environ.get("MONGODB_PWD")
username = os.environ.get("MONGODB_NAME")
conn_string = f"mongodb+srv://{username}:{password}@mongoapi.0ix5n.mongodb.net/"

client = MongoClient(conn_string)

db = client.todo_db

collection_name = db["todo_collection"]