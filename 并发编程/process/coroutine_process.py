# -*- coding: utf-8 -*-
import asyncio
import httpx
from aiomultiprocess import Pool

"""
协程与多进程相结合
from aiomultiprocess import Pool
async with Pool() as pool:
    results = await pool.map(协程, 参数列表)  # 返回迭代器
"""


async def get(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text


async def main():
    urls = ["url1", "url2", "url3"]
    async with Pool() as pool:
        async for result in pool.map(get, urls):
            print(result)


if __name__ == "__main__":
    asyncio.run(main())
