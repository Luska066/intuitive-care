from sqlalchemy import Column, Integer, String
from FastApi.Adaptors.MysqlDatabase import BASE


class Operadora(BASE):
    __tablename__ = "OPERADORAS"

    id = Column(Integer, primary_key=True, index=True)
    Registro_ANS = Column(String(255), unique=True, index=True)
    CNPJ = Column(String(255))
    Razao_Social = Column(String(1000))
    Nome_Fantasia = Column(String(1000))
    Modalidade = Column(String(1000))
    Logradouro = Column(String(1000))
    Numero = Column(String(255))
    Complemento = Column(String(255))
    Bairro = Column(String(255))
    Cidade = Column(String(255))
    UF = Column(String(3))
    CEP = Column(String(255))
    DDD = Column(String(3))
    Telefone = Column(String(20))
    Fax = Column(String(255))
    Endereco_eletronico = Column(String(255))
    Representante = Column(String(300))
    Cargo_Representante = Column(String(255))
    Regiao_de_Comercializacao = Column(String(255))
    Data_Registro_ANS = Column(String(255))