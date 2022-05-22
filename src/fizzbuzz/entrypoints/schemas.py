from pydantic import BaseModel


class FizzBuzzIn(BaseModel):
    int1: int
    int2: int
    limit: int
    str1: str
    str2: str


class FizzBuzzOut(BaseModel):
    computed_string: str
