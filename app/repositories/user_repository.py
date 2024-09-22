from typing import List

from bson import ObjectId
from mongoengine import ValidationError

from app.models import User
from app.models.input import UserInput


class UserRepository:

    def create(self, user_input: UserInput) -> User:
        return User(**user_input.model_dump()).save()

    def update(self, identifier: str | ObjectId, user_input: UserInput) -> User | None:
        update_config = dict()
        update_config.update(
            {f"set__{field}": value for field, value in user_input.model_dump().items()}
        )
        User.objects(id=identifier).update_one(**update_config)
        return self.find_by_id(identifier)

    def find_by_id(self, identifier: str | ObjectId) -> User | None:
        try:
            return User.objects(id=identifier).first()
        except ValidationError:
            return None

    def get_all(self) -> List[User]:
        return User.objects()

    def get_all_paginated(self, start: int, limit: int) -> List[User]:
        return User.objects.skip(start - 1).limit(limit)

    def delete(self, identifier: str) -> None:
        try:
            user: User = User.objects(id=identifier).only("id").first()
            if user:
                user.delete()
        except ValidationError:
            return None

    def count(self):
        return User.objects.count()
