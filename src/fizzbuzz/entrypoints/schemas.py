from pydantic import BaseModel


class FizzBuzzIn(BaseModel):
    int1: int
    int2: int
    limit: int = 15
    str1: str
    str2: str
