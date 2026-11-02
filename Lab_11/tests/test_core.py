import asyncio

import pytest
from lab import async_map
@pytest.mark.asyncio
async def test_async_map_order():
 async def double(x):
  await asyncio.sleep(0); return x*2
 assert await async_map(double,[1,2,3],limit=2)==[2,4,6]
