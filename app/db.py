import os

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, declared_attr

postgres_host = os.getenv("POSTGRES_HOST", "localhost")
engine = create_engine(f'postgresql://postgres:example@{postgres_host}:5432/postgres', echo=True)


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)


class Secret(Base):
    __tablename__ = 'secret'
    secret = Column(String(200))
    secret_key = Column(String(200))


Base.metadata.create_all(engine)
