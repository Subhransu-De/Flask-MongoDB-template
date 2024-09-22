from typing import List

from injector import inject

from app.models.input import UserInput
from app.models.output import UserOutput
from app.repositories import UserRepository


class UserService:
    @inject
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def create(self, user_input: UserInput) -> UserOutput:
        created_user = self._user_repository.create(user_input)
        return UserOutput.from_(created_user)

    def get(self, user_id) -> UserOutput:
        pass

    def get_all(self) -> List[UserOutput]:
        pass

    def update(self, user_id, user: UserInput) -> UserOutput:
        pass

    def delete(self, user_id) -> None:
        pass

    def get_paginated(self, page, per_page):
        pass
