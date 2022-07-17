from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy import MetaData
from sqlalchemy.orm import Session

from web_api import schemas, crud
from web_api.database import Base, sessionLocal, engine

Base.metadata.create_all(bind=engine)
app = FastAPI()
meta = MetaData(bind=engine)


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/records')
def create_record(sc_record: schemas.Record, db: Session = Depends(get_db)):
    crud.create_record(db, sc_record)
    return 'ok'


@app.get('/records', response_model=List[schemas.Record])
def read_records(db: Session = Depends(get_db)):
    records = crud.read_records(db, {})
    return records


@app.get('/records/filter_by_id/{record_id}', response_model=List[schemas.Record])
def read_records_by_id(record_id: int, db: Session = Depends(get_db)):
    records = crud.read_records(db, {'id': record_id})
    return records


@app.get('/records/filter_by_name/{record_name}', response_model=List[schemas.Record])
def read_records_by_name(record_name: str, db: Session = Depends(get_db)):
    records = crud.read_records(db, {'name': record_name})
    return records


@app.put('/records')
def update_record(record_id: int, sc_record: schemas.Record, db: Session = Depends(get_db)):
    crud.update_record(db, record_id, sc_record)
    return 'ok'


@app.delete('/records')
def delete_record(record_id: int, db: Session = Depends(get_db)):
    crud.delete_record(db, record_id)
    return 'ok'
