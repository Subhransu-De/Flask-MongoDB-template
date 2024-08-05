from typing import Optional

from pymongo import MongoClient
from pymongo.database import Database

client: Optional[MongoClient] = None
db: Optional[Database] = None


def init_db(app):
    global client, db
    client = MongoClient(app.config["MONGO_URI"])
    db = client[app.config["MONGO_DB_NAME"]]


def get_db() -> Database:
    if db is None:
        raise RuntimeError("Database not initialized. Call init_db() first.")
    return db
