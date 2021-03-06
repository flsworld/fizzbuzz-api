from typing import Any

import pytest

from src.fizzbuzz.cache import AbstractInMemoryCache


@pytest.fixture
def cache():
    class InMemoryCacheTest(AbstractInMemoryCache):
        async def get(self, key: str):
            return self.store.get(key)

        async def set(self, key: str, value: Any):
            self.store[key] = value

        def clear(self):
            self.store.clear()

    cache = InMemoryCacheTest()
    yield cache
    cache.clear()
