from typing import List

from ..database import get_db
from ..models.input.user_input import UserInput
from ..models.output.user_output import UserOutput
from ..repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.repository = UserRepository(get_db())

    def create_user(self, user_input: UserInput) -> UserOutput:
        return UserOutput(**self.repository.create(user_input).model_dump())

    def get_user(self, user_id) -> UserOutput | None:
        user = self.repository.find_by_id(user_id)
        if user:
            return UserOutput(**user.model_dump())
        else:
            return None

    def get_all_users(self) -> List[UserOutput]:
        users: List[UserOutput] = []
        for user in self.repository.find_all():
            users.append(UserOutput(**user.model_dump()))
        return users

    def update_user(self, user_id, user_data):
        return self.repository.update(user_id, user_data)

    def delete(self, user_id) -> None:
        self.repository.delete(user_id)

    def get_users_paginated(self, page, per_page):
        return self.repository.find_all_paginated(page, per_page)
