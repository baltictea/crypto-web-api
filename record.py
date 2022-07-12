from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()


class RequestRecord(BaseModel):
    name: str
    rate: float
    datetime: str


class DatabaseRecord(Base):
    __tablename__ = 'crypto_exchange_rate'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    rate = Column(Float)
    datetime = Column(String)

    def __init__(self, request: RequestRecord):
        self.name = request.name
        self.rate = request.rate
        self.datetime = request.datetime