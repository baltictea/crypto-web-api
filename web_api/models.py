from sqlalchemy import Column, Integer, String, Float

from web_api.database import Base


class DatabaseRecord(Base):
    __tablename__ = 'crypto_exchange_rate'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    rate = Column(Float)
    datetime = Column(String)

