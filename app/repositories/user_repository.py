from typing import List

from bson import ObjectId
from bson.errors import InvalidId
from injector import inject

from .. import MongoDatabase
from ..models.input.user_input import UserInput
from ..models.user import User


class UserRepository:

    @inject
    def __init__(self, mongodb: MongoDatabase):
        self.collection = mongodb.db.users

    def create(self, user_input: UserInput) -> User:
        result = self.collection.insert_one(user_input.model_dump())
        return self.find_by_id(str(result.inserted_id))

    def find_by_id(self, identifier: str) -> User:
        user: User | None = None
        try:
            user_raw = self.collection.find_one(filter={"_id": ObjectId(identifier)})
            if user_raw:
                user_raw["id"] = str(user_raw["_id"])
                user = User(**user_raw)
        except InvalidId:
            pass  # TODO: Exception is eaten up.
        finally:
            return user

    def find_all(self) -> List[User]:
        users: List[User] = []
        for user in list(self.collection.find()):
            user["id"] = str(user["_id"])
            users.append(User(**user))
        return users

    def update(self, identifier: str, data: UserInput) -> User:
        result = self.collection.update_one(
            {"_id": ObjectId(identifier)}, {"$set": data.model_dump()}
        )
        return self.find_by_id(identifier)

    def delete(self, identifier) -> None:
        try:
            self.collection.delete_one({"_id": ObjectId(identifier)})
        except InvalidId:
            pass

    def find_all_paginated(self, page, per_page):
        total = self.collection.count_documents({})
        users = list(self.collection.find().skip((page - 1) * per_page).limit(per_page))

        for user in users:
            user["_id"] = str(user["_id"])

        return {
            "users": users,
            "page": page,
            "per_page": per_page,
            "total": total,
            "pages": (total + per_page - 1),
        }
