from bson import ObjectId

from app.models import User


class UserRepository:

    def create(self) -> User:
        pass

    def update(self) -> User:
        pass

    def find_by_id(self, identifier: str | ObjectId) -> User:
        pass

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
