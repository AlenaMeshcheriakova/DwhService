from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from cfg.сonfig import settings
from src.db.base import Base

# --------------------WORK WITH ENGINE--------------------

sync_engine = create_engine(
    url=settings.DATABASE_DWH_URL_psycopg,
    echo=True,
    pool_size=15,
)

session_factory = sessionmaker(sync_engine)

def get_session():
    with session_factory() as session:
        yield session

def create_db_and_tables():
    Base.metadata.create_all(sync_engine)