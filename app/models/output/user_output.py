from pydantic import BaseModel, Field


class UserOutput(BaseModel):
    id: str = Field(default=None, serialization_alias="id")
    username: str = Field(default=None, serialization_alias="username")
    email: str = Field(default=None, serialization_alias="email")
    age: int = Field(default=None, serialization_alias="age")
