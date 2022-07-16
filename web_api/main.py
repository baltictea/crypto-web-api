from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session

from web_api import schemas, crud
from web_api.database import Base, sessionLocal, engine

Base.metadata.create_all(bind=engine)
app = FastAPI()
engine = create_engine('sqlite:///database.sqlite')
meta = MetaData(bind=engine)


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/records')
def create_record(sc_record: schemas.RecordCreate, db: Session = Depends(get_db)):
    crud.create_record(db, sc_record)
    return 'ok'


@app.get('/records', response_model=List[schemas.Record])
def read_records(db: Session = Depends(get_db)):
    records = crud.read_records(db, True)
    return records


@app.delete('/records')
def delete_record(record_id: int, db: Session = Depends(get_db)):
    crud.delete_record(db, record_id)
    return 'ok'


@app.put('/records')
def update_record(record_id: int, sc_record: schemas.RecordCreate, db: Session = Depends(get_db)):
    crud.update_record(db, record_id, sc_record)
    return 'ok'

# @app.get('/')
# def get_table_names():
#    return engine.table_names()
