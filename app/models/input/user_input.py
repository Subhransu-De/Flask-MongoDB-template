from pydantic import BaseModel


class UserInput(BaseModel):
    username: str
    email: str
    age: int
