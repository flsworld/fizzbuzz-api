import json

import pytest

from src.fizzbuzz.cache import update_cache, AbstractInMemoryCache


class InMemoryCacheTest(AbstractInMemoryCache):
    async def get(self, key: str):
        return self.store.get(key)

    async def set(self, key: str, count: int):
        self.store[key] = count


@pytest.mark.asyncio
async def test_update_cache():
    params = {
        "int1": 77,
        "int2": 255,
        "limit": 1_500,
        "str1": "bonjour",
        "str2": "aurevoir",
    }
    cache = InMemoryCacheTest()

    await update_cache(params, cache)

    key = json.dumps(params)
    expected = 1
    assert await cache.get(key) == expected


@pytest.mark.asyncio
async def test_update_cache_when_called_multiple_times():
    params = {
        "int1": 2,
        "int2": 12,
        "limit": 1_500,
        "str1": "fizz",
        "str2": "buzz",
    }
    cache = InMemoryCacheTest()

    await update_cache(params, cache)
    await update_cache(params, cache)
    await update_cache(params, cache)

    key = json.dumps(params)
    expected = 3
    assert await cache.get(key) == expected
