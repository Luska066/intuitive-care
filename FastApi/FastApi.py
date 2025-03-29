from typing import Union

from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import Session

from Adaptors.MysqlDatabase import BASE,engine,SESSION
from Repository.OperadoraRepository import OperadoraRepository

app = FastAPI()

BASE.metadata.create_all(bind=engine)

def get_db():
    db = SESSION()
    try:
        yield db
    finally:
        db.close()

@app.get("/contabiliade")
def read_item(db: Session = Depends(get_db)):
    return OperadoraRepository.getAll()

@app.get("/contabiliade/{registro_ans}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}