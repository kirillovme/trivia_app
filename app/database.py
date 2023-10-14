import logging

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from app.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_async_engine(DATABASE_URL)
Base = declarative_base()
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_db():
    logging.info('Connecting to the database.')
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    db = async_session()
    try:
        yield db
    finally:
        logging.info('Closing the database connection.')
        await db.close()
