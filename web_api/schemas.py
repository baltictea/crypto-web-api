from pydantic import BaseModel


class RecordBase(BaseModel):
    name: str
    rate: str


class Record(RecordBase):
    id: int
    datetime: str

    class Config:
        orm_mode = True
