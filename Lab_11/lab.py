"""Async functional mapping with explicit IO boundary."""
import asyncio
from collections.abc import Awaitable, Callable, Iterable
from typing import TypeVar
T=TypeVar("T"); U=TypeVar("U")
async def async_map(function: Callable[[T],Awaitable[U]], values: Iterable[T], limit: int=5) -> list[U]:
    if limit<1: raise ValueError("limit must be positive")
    semaphore=asyncio.Semaphore(limit)
    async def guarded(value:T) -> U:
        async with semaphore: return await function(value)
    return list(await asyncio.gather(*(guarded(value) for value in values)))
async def fetch_length(text: str) -> int:
    await asyncio.sleep(0); return len(text)
async def main() -> None: print(await async_map(fetch_length,["functional","python","async"]))
if __name__=="__main__": asyncio.run(main())
