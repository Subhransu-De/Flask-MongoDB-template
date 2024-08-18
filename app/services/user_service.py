from typing import List

from injector import inject

from .. import UserRepository
from ..exception.not_found_exception import NotFoundException
from ..models.input.user_input import UserInput
from ..models.output.user_output import UserOutput


class UserService:
    @inject
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create(self, user_input: UserInput) -> UserOutput:
        return UserOutput(**self.user_repository.create(user_input).model_dump())

    def get(self, user_id) -> UserOutput:
        user = self.user_repository.find_by_id(user_id)
        if user:
            return UserOutput(**user.model_dump())
        else:
            raise NotFoundException(f"User with id {user_id} not found.")

    def get_all(self) -> List[UserOutput]:
        users: List[UserOutput] = []
        for user in self.user_repository.find_all():
            users.append(UserOutput(**user.model_dump()))
        return users

    def update(self, user_id, user: UserInput) -> UserOutput:
        if not self.user_repository.find_by_id(user_id):
            raise NotFoundException(f"User with id {user_id} not found.")
        return UserOutput(**self.user_repository.update(user_id, user).model_dump())

    def delete(self, user_id) -> None:
        self.user_repository.delete(user_id)

    def get_paginated(self, page, per_page):
        return self.user_repository.find_all_paginated(page, per_page)
