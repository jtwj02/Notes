from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

from .config import settings

DATABASE_URL = (
    f"postgresql+asyncpg://{settings.database_username}:"
    f"{settings.database_password}@{settings.database_hostname}:"
    f"{settings.database_port}/{settings.database_name}"
)

engine = create_async_engine(DATABASE_URL)
async_session = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()

async def async_session():
    async with async_session() as session:
        yield session

