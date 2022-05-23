from pydantic import BaseModel


class FizzBuzzIn(BaseModel):
    """
    Pydantic model that deal with input data of compute_string operation
    """
    int1: int = 3
    int2: int = 5
    limit: int = 15
    str1: str = "fizz"
    str2: str = "buzz"
