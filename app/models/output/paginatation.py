from typing import TypeVar, Generic, List

from pydantic import BaseModel

T = TypeVar("T")


class Paginated(BaseModel, Generic[T]):
    total: int
    start: int
    limit: int
    items: List[T]
