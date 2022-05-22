from typing import Optional

from src.fizzbuzz.cache import InMemoryCache
from src.fizzbuzz.service_layer.exceptions import CannotCompute


def compute_fizzbuzz(int1: int, int2: int, limit: int, str1: str, str2: str) -> str:
    if int1 == int2:
        raise CannotCompute("'Multiple of' inputs are identical")
    if 0 in (int1, int2):
        raise CannotCompute("'Multiple of' zero as input is not possible")

    output = []
    i = 1
    while i <= limit:
        if i % int1 == 0 and i % int2 == 0:
            output.append(str1 + str2)
        elif i % int1 == 0:
            output.append(str1)
        elif i % int2 == 0:
            output.append(str2)
        else:
            output.append(str(i))
        i += 1
    return ",".join(output)


def most_popular_request() -> Optional[dict]:
    cache = InMemoryCache.store
    if not cache:
        return

    most_hit = max(cache, key=cache.get)
    return {most_hit: cache.get(most_hit)}
