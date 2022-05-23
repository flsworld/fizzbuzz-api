import json

import pytest

from src.fizzbuzz.cache import update_cache


@pytest.mark.asyncio
async def test_update_cache(cache):
    params = {
        "int1": 77,
        "int2": 255,
        "limit": 1_500,
        "str1": "bonjour",
        "str2": "aurevoir",
    }

    await update_cache(params, cache)

    key = json.dumps(params)
    expected = 1
    assert await cache.get(key) == expected


@pytest.mark.asyncio
async def test_update_cache_when_called_multiple_times(cache):
    params = {
        "int1": 2,
        "int2": 12,
        "limit": 1_500,
        "str1": "fizz",
        "str2": "buzz",
    }

    await update_cache(params, cache)
    await update_cache(params, cache)
    await update_cache(params, cache)

    key = json.dumps(params)
    expected = 3
    assert await cache.get(key) == expected
