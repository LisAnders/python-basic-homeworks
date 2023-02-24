"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base, declared_attr, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

async_engine: AsyncEngine = create_async_engine(url=PG_CONN_URI, echo=True)


class Base:
    @declared_attr
    def __tablename__(cls):
        """
        User -> tbl_users
        Post -> tbl_posts
        """
        return f"tbl_{cls.__name__.lower()}s"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


Base = declarative_base(cls=Base)
Session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


class User(Base):
    name = Column(String, unique=False, nullable=False)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    posts = relationship("Post", back_populates="user")


class Post(Base):
    user_id = Column(Integer, ForeignKey(User.id), unique=False, nullable=False)
    title = Column(String, unique=False, nullable=False)
    body = Column(String, unique=False, nullable=False)
    user = relationship("User", back_populates="posts")
