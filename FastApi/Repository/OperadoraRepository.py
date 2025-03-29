from sqlalchemy.orm import Session
from FastApi.Models.Operadora import Operadora

class OperadoraRepository:

    def getAll(self,db:Session):
        return db.query(Operadora).all()