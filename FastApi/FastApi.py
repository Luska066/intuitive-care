from typing import Union

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .Adaptors.MysqlDatabase import BASE,engine,SESSION
from .Repository.OperadoraRepository import OperadoraRepository

app = FastAPI()

BASE.metadata.create_all(bind=engine)

origins = [
    "http://localhost:9000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SESSION()
    try:
        yield db
    finally:
        db.close()

@app.get("/contabilidade")
def read_item(db: Session = Depends(get_db)):
    return OperadoraRepository().getAll(db)

@app.get("/contabilidade/{registro_ans}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}