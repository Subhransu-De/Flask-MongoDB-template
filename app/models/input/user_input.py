from pydantic import BaseModel, Field, EmailStr, PositiveInt


class UserInput(BaseModel):
    username: str = Field(min_length=3, max_length=50, alias="username")
    email: EmailStr = Field(alias="email")
    age: PositiveInt = Field(ge=0, le=120, alias="age")
