from pymongo import MongoClient
from pymongo.database import Database


class MongoDatabase:
    client: MongoClient
    db: Database

    def __init__(self, uri: str, database_name: str):
        self.client = MongoClient(uri)
        self.db = self.client.get_database(database_name)
