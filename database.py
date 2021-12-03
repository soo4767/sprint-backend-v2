import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ROOT_PATH = Path(os.path.realpath(__file__)).parent.absolute()

SQLALCHAMY_DATABASE_URL = f"sqlite+pysqlite:///{ROOT_PATH}/sprint.db"

engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, )

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
