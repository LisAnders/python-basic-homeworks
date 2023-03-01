"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def get_data(url: str) -> list[dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data


async def users_data() -> list[dict]:
    users: list[dict] = await get_data(USERS_DATA_URL)
    return users


async def posts_data() -> list[dict]:
    posts = await get_data(POSTS_DATA_URL)
    return posts


async def main():
    result_users = await users_data()
    result_posts = await posts_data()
    print(f"result_users -> {result_users}")
    print(f"result_posts -> {result_posts}")


if __name__ == '__main__':
    asyncio.run(main())
