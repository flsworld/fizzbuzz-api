import json
from asyncio import Lock


class AbstractInMemoryCache:
    store = {}

    async def get(self, key: str):
        raise NotImplementedError

    async def set(self, key: str, count: int):
        raise NotImplementedError


class InMemoryCache(AbstractInMemoryCache):
    _lock = Lock()

    async def get(self, key: str) -> int:
        async with self._lock:
            return self.store.get(key)

    async def set(self, key: str, count: int):
        async with self._lock:
            self.store[key] = count


async def update_cache(params: dict, cache: AbstractInMemoryCache):
    cache_key = json.dumps(params)
    if count := await cache.get(cache_key):
        count += 1
    else:
        count = 1

    await cache.set(cache_key, count)
