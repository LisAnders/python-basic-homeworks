"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from models import Base, Session, User, Post, async_engine
from jsonplaceholder_requests import users_data, posts_data


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_user(session: AsyncSession, name: str, username: str, email: str) -> User:
    user = User(name=name, username=username, email=email)
    session.add(user)
    await session.commit()
    return user


async def create_post(session: AsyncSession, user_id: int, title: str, body: str) -> Post:
    post = Post(user_id=user_id, title=title, body=body)
    session.add(post)
    await session.commit()
    return post


async def async_main():
    async with Session() as session:
        await create_tables()
        user_data, post_data = await asyncio.gather(users_data(), posts_data())
        for user in user_data:
            await create_user(
                session=session,
                name=user.get('name'),
                username=user.get('username'),
                email=user.get('email'),
            )
        for post in post_data:
            await create_post(
                session=session,
                user_id=int(post.get('userId')),
                title=post.get('title'),
                body=post.get('body'),
            )


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
