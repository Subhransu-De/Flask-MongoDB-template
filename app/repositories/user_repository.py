from typing import List

from bson import ObjectId
from mongoengine import ValidationError

from app.models import User
from app.models.input import UserInput


class UserRepository:

    def create(self, user_input: UserInput) -> User:
        return User(**user_input.model_dump()).save()

    def update(self, identifier: str | ObjectId, user_input: UserInput) -> User:
        pass

    def find_by_id(self, identifier: str | ObjectId) -> User | None:
        try:
            return User.objects(id=identifier).first()
        except ValidationError:
            return None

    def get_all(self) -> List[User]:
        return User.objects()

    def find_all_paginated(self, page, per_page) -> User:
        pass
        # total = self.collection.count_documents({})
        # users = list(self.collection.find().skip((page - 1) * per_page).limit(per_page))
        #
        # for user in users:
        #     user["_id"] = str(user["_id"])
        #
        # return {
        #     "users": users,
        #     "page": page,
        #     "per_page": per_page,
        #     "total": total,
        #     "pages": (total + per_page - 1),
        # }

    def delete(self, identifier: str) -> None:
        try:
            user: User = User.objects(id=identifier).only("id").first()
            if user:
                user.delete()
        except ValidationError:
            return None
