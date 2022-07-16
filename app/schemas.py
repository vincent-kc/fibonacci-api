from pydantic import BaseModel, PositiveInt
from typing import Union

from app.models import Status


class FibInput(BaseModel):
    n: PositiveInt


class FibOutput(BaseModel):
    nth: Union[str, None] = None
    status: Status

    class Config:
        orm_mode = True
