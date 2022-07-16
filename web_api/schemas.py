from pydantic import BaseModel


class RecordBase(BaseModel):
    name: str
    rate: str


class RecordCreate(RecordBase):
    datetime: str


class Record(RecordBase):
    datetime: str
    id: int

    class Config:
        orm_mode = True
