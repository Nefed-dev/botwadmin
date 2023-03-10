from sqlalchemy.orm import declarative_base
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from settings import settings

engine = create_engine(url=settings.db_dsn())
session_maker = sessionmaker(engine)
Session = scoped_session(session_maker)

async_engine = create_async_engine(url=settings.db_dsn())
async_session = async_sessionmaker(async_engine)

metadata = MetaData()
Base = declarative_base(metadata=metadata)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        return session


def create_tables():
    Base.metadata.create_all(engine)
    Session.commit()


if __name__ == "__main__":
    create_tables()
