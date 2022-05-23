import json

import pytest

from src.fizzbuzz.cache import update_cache, most_popular_request, MostPopular


@pytest.mark.asyncio
async def test_update_cache_when_key_not_in_cache(cache):
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
async def test_update_cache_when_key_in_cache(cache):
    params = {
        "int1": 77,
        "int2": 255,
        "limit": 1_500,
        "str1": "bonjour",
        "str2": "aurevoir",
    }
    await cache.set(json.dumps(params), 6)

    await update_cache(params, cache)

    key = json.dumps(params)
    expected = 7
    assert await cache.get(key) == expected


@pytest.mark.asyncio
async def test_update_cache_when_most_popular_key_not_in_cache(cache):
    params = {
        "int1": 77,
        "int2": 255,
        "limit": 1_500,
        "str1": "bonjour",
        "str2": "aurevoir",
    }

    await update_cache(params, cache)

    most_popular = await cache.get("most_popular")
    assert json.loads(most_popular.request) == params
    assert most_popular.count == 1


@pytest.mark.asyncio
async def test_update_cache_when_most_popular_key_already_in_cache(cache):
    former_request = MostPopular("request", 77)
    await cache.set("most_popular", former_request)

    await update_cache({"int1": 2}, cache)

    most_popular = await cache.get("most_popular")
    assert most_popular.request == former_request.request
    assert most_popular.count == former_request.count


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


@pytest.mark.asyncio
async def test_most_popular_request_should_return_most_hit_request(cache):
    most_popular = MostPopular('{"int1": 3, "int2": 5}', 7)
    await cache.set("most_popular", most_popular)

    res = await most_popular_request(cache)

    request = json.loads(most_popular.request)
    assert res == {**request, "number_of_hit": most_popular.count}


@pytest.mark.asyncio
async def test_most_popular_request_when_json_decode_error_should_return_most_hit_request(cache):
    most_popular = MostPopular("request1", 3)
    await cache.set("most_popular", most_popular)

    res = await most_popular_request(cache)

    assert res == {"request": most_popular.request, "number_of_hit": most_popular.count}


@pytest.mark.asyncio
async def test_most_popular_request_when_cache_is_empty_should_return_none(cache):

    res = await most_popular_request(cache)

    assert res is None
