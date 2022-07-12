from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from record import DatabaseRecord, Base


def create_database(engine):
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    #session.add(Record(name='', rate='0.0', datetime=''))
    session.commit()
