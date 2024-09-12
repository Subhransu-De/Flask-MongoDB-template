from typing import Optional

from pydantic import BaseModel, Field


class UserOutput(BaseModel):
    id: Optional[str] = Field(serialization_alias="id")
    username: Optional[str] = Field(serialization_alias="username")
    email: Optional[str] = Field(serialization_alias="email")
    age: Optional[int] = Field(serialization_alias="age")
