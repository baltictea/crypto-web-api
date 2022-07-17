from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session

from web_api import models
from web_api import schemas

app = FastAPI()
engine = create_engine('sqlite:///database.sqlite')
meta = MetaData(bind=engine)


def create_record(db: Session, sc_record: schemas.Record):
    record = models.DatabaseRecord(
        name=sc_record.name,
        rate=sc_record.rate,
        datetime=sc_record.datetime
    )
    db.add(record)
    db.commit()
    db.refresh(record)


def read_records(db: Session, search_filter):
    return db \
        .query(models.DatabaseRecord) \
        .filter_by(**search_filter) \
        .all()


def update_record(db: Session, record_id: int, sc_record: schemas.Record):
    record = db \
        .query(models.DatabaseRecord) \
        .where(models.DatabaseRecord.id == record_id) \
        .first()
    record.name = sc_record.name
    record.rate = sc_record.rate
    record.datetime = sc_record.datetime
    db.add(record)
    db.commit()
    db.refresh(record)


def delete_record(db: Session, record_id: int):
    db.query(models.DatabaseRecord).where(models.DatabaseRecord.id == record_id).delete()
    db.commit()
