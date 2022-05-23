from pydantic import BaseModel


class FizzBuzzIn(BaseModel):
    int1: int = 3
    int2: int = 5
    limit: int = 15
    str1: str = "fizz"
    str2: str = "buzz"
