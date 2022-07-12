from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData, delete
from sqlalchemy.orm import Session

from database import create_database
from record import DatabaseRecord, RequestRecord

app = FastAPI()
engine = create_engine('sqlite:///database.sqlite')
meta = MetaData(bind=engine)


@app.get('/')
def get_table_names():
    return engine.table_names()


# TODO: сделать для любой таблицы
@app.get('/records/list')
def get_record_list():
    session = Session(bind=engine)
    records = session.query(DatabaseRecord).all()
    session.close()
    return records


@app.post('/records/add')
def add_record(request: RequestRecord):
    session = Session(bind=engine)
    session.add(DatabaseRecord(request))
    session.commit()
    session.close()
    return {'status': 'ok'}


@app.get('/records/create')
def create_records_table():
    create_database(engine)
    return {'status': 'ok'}


@app.delete('/records/delete')
def delete_record(id_: int):
    session = Session(bind=engine)
    statement = delete(DatabaseRecord).where(DatabaseRecord.id == id_)
    session.execute(statement)
    session.commit()
    session.close()
    return {'status': 'ok'}


@app.put('/records/update')
def update_record(id_: int, request: RequestRecord):
    session = Session(bind=engine)
    session \
        .query(DatabaseRecord).where(DatabaseRecord.id == id_) \
        .update({'name': request.name, 'rate': request.rate, 'datetime': request.datetime})
    session.commit()
    session.close()
    return {'status': 'ok'}
