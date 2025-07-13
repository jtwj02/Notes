from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from .config import settings

DATABASE_URL = (
    f"postgresql+asyncpg://{settings.database_username}:"
    f"{settings.database_password}@{settings.database_hostname}:"
    f"{settings.database_port}/{settings.database_name}"
)

engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
