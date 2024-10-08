from pydantic import BaseModel, Field

from app.models import User


class UserOutput(BaseModel):
    id: str = Field(default=None, serialization_alias="id")
    username: str = Field(default=None, serialization_alias="username")
    email: str = Field(default=None, serialization_alias="email")
    age: int = Field(default=None, serialization_alias="age")

    @staticmethod
    def from_(data: User, **kwargs) -> "UserOutput":
        return UserOutput(id=str(data.id), **data.to_mongo().to_dict(), **kwargs)
