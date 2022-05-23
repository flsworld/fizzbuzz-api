import json
from asyncio import Lock


class AbstractInMemoryCache:
    store = {}

    async def get(self, key: str):
        raise NotImplementedError

    async def set(self, key: str, count: int):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError


class InMemoryCache(AbstractInMemoryCache):
    _lock = Lock()

    async def get(self, key: str) -> int:
        async with self._lock:
            return self.store.get(key)

    async def set(self, key: str, count: int):
        async with self._lock:
            self.store[key] = count

    def clear(self):
        self.store.clear()


async def update_cache(params: dict, cache: AbstractInMemoryCache):
    """
    Add or update count in cache for a given set of params in input. The chosen key format is a JSON
    formatted string
    """
    cache_key = json.dumps(params)
    if count := await cache.get(cache_key):
        count += 1
    else:
        count = 1

    await cache.set(cache_key, count)
