from typing import Optional

from pydantic import BaseModel


class UserOutput(BaseModel):
    id: Optional[str]
    username: Optional[str]
    email: Optional[str]
    age: Optional[int]
