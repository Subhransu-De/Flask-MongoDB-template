from typing import List

from injector import inject

from app.exception import NotFoundException
from app.models import User
from app.models.input import UserInput
from app.models.output import UserOutput
from app.repositories import UserRepository


class UserService:
    @inject
    def __init__(self, user_repository: UserRepository):
        self._repository = user_repository

    def create(self, user_input: UserInput) -> UserOutput:
        created_user: User = self._repository.create(user_input)
        return UserOutput.from_(created_user)

    def get(self, user_id: str) -> UserOutput:
        fetched_user: User = self._repository.find_by_id(user_id)
        if fetched_user is None:
            raise NotFoundException(f"User with id {user_id} not found.")
        return UserOutput.from_(fetched_user)

    def get_all(self) -> List[UserOutput]:
        return [
            UserOutput.from_(fetched_user)
            for fetched_user in self._repository.get_all()
        ]

    def update(self, user_id: str, user_input: UserInput) -> UserOutput:
        updated_user: User = self._repository.update(user_id, user_input)
        if updated_user is None:
            raise NotFoundException(f"User with id {user_id} not found.")
        return UserOutput.from_(updated_user)

    def delete(self, user_id) -> None:
        self._repository.delete(user_id)

    def get_paginated(self, page, per_page):
        pass
