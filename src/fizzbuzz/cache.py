import json
from asyncio import Lock
from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class MostPopular:
    request: str
    count: int


class AbstractInMemoryCache:
    store = {}

    async def get(self, key: str):
        raise NotImplementedError

    async def set(self, key: str, value: Any):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError


class InMemoryCache(AbstractInMemoryCache):
    _lock = Lock()

    async def get(self, key: str) -> Any:
        async with self._lock:
            return self.store.get(key)

    async def set(self, key: str, value: Any):
        async with self._lock:
            self.store[key] = value

    def clear(self):
        self.store.clear()


async def update_cache(params: dict, cache: AbstractInMemoryCache):
    """
    Store in cache the request and its number of hits. Update the most used request when needed
    """
    cache_key = json.dumps(params)
    if not await cache.get("most_popular"):
        await cache.set("most_popular", MostPopular(cache_key, 1))

    if cache_key not in cache.store:
        await cache.set(cache_key, 1)
    else:
        count = await cache.get(cache_key)
        new_count = count + 1
        await cache.set(cache_key, new_count)
        # Set the most popular key in cache
        most_popular = await cache.get("most_popular")
        if new_count > most_popular.count:
            await cache.set("most_popular", MostPopular(cache_key, new_count))


async def most_popular_request(cache: AbstractInMemoryCache) -> Optional[dict]:
    """
    Return the most hit request in cache if the cache is not empty
    """
    most_popular: MostPopular = await cache.get("most_popular")
    if not most_popular:
        return
    try:
        request = json.loads(most_popular.request)
    except json.JSONDecodeError:
        return {"request": most_popular.request, "number_of_hit": most_popular.count}
    else:
        return {
            **request,
            "number_of_hit": most_popular.count
        }
