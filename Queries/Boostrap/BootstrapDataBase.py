# LIBS
import os
import csv
from time import sleep

from Selenium.Enums.DirectoryEnum import DirectoryEnum
from Adaptors.Mysql import Mysql


class BootstrapDataBase:
    directory_accounting_demonstration = DirectoryEnum.PDF.value + "/AccountingDemonstration"
    directory_active_operators = DirectoryEnum.PDF.value + "/ActiveOperators"
    mysql = Mysql()

    def initTables(self):
        statement = self.mysql.create()
        statement.cursor().execute("""
               CREATE TABLE IF NOT EXISTS  CONTABILIDADE(
                    id int primary key auto_increment not null,
                    DATA varchar(255),
                    REG_ANS varchar(255),
                    DESCRICAO text,
                    CD_CONTA_CONTABIL varchar(1000),
                    VL_SALDO_INICIAL float,
                    VL_SALDO_FINAL float
                );
            """)

        statement.cursor().execute("""
           CREATE TABLE IF NOT EXISTS  OPERADORAS(
                id int primary key auto_increment not null,
                Registro_ANS varchar(255),
                CNPJ varchar(255),
                Razao_Social varchar(1000),
                Nome_Fantasia varchar(1000),
                Modalidade varchar(1000),
                Logradouro varchar(1000),
                Numero varchar(255),
                Complemento varchar(255),
                Bairro varchar(255),
                Cidade varchar(255),
                UF varchar(3),
                CEP varchar(255),
                DDD varchar(3),
                Telefone varchar(20),
                Fax varchar(255),
                Endereco_eletronico varchar(255),
                Representante varchar(300),
                Cargo_Representante varchar(255),
                Regiao_de_Comercializacao varchar(255),
                Data_Registro_ANS varchar(255)
            );
        """)

    def runOperators(self):
        statement = self.mysql.create()
        for roots, dirs, files in os.walk(self.directory_active_operators):
            for file in files:
                if file.endswith(".csv"):
                    file_path = os.path.join(roots, file)
                    with open(file_path, 'r', encoding='utf-8') as file:
                        csv_reader = csv.reader(file, delimiter=';')
                        headers = next(csv_reader)
                        execute_statement = statement.cursor()
                        for row in csv_reader:
                            row = [value.strip('"') if value.strip() else None for value in row]  # Limpeza de dados
                            if not self.findOperadorasByRegistroANS(row[0]):
                                execute_statement.execute("""
                                         INSERT INTO OPERADORAS
                                         (Registro_ANS,
                                         CNPJ,
                                         Razao_Social,
                                         Nome_Fantasia,
                                         Modalidade,
                                         Logradouro,
                                         Numero,
                                         Complemento,
                                         Bairro,
                                         Cidade,
                                         UF,
                                         CEP,
                                         DDD,
                                         Telefone,
                                         Fax,
                                         Endereco_eletronico,
                                         Representante,
                                         Cargo_Representante,
                                         Regiao_de_Comercializacao,
                                         Data_Registro_ANS
                                         ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                   """, row[:20])
                                statement.commit()
                            else:
                                print("Registro ANS" + row[0] + " já existe")

    def findOperadorasByRegistroANS(self, Registro_ANS):
        statement = self.mysql.create()
        execute_statement = statement.cursor()
        execute_statement.execute("""
             SELECT (Registro_ANS) FROM OPERADORAS WHERE Registro_ANS = %s 
       """, [Registro_ANS])
        resultado = execute_statement.fetchone()
        if resultado:
            return True
        else:
            return False

    def runContability(self):
        statement = self.mysql.create()
        for roots, dirs, files in os.walk(self.directory_accounting_demonstration):
            for file in files:
                if file.endswith(".csv") and roots.split("/")[-1] == 'csv':
                    file_path = os.path.join(roots, file)
                    print("Lendo arquivo : " + file)
                    sleep(2)
                    with open(file_path, 'r', encoding='utf-8') as file:
                        csv_reader = csv.reader(file, delimiter=';')
                        headers = next(csv_reader)
                        for row in csv_reader:
                            rows = [
                                str(row[0]),
                                str(row[1]),
                                str(row[2]),
                                str(row[3]),
                                float(row[4].replace(',', '.')),
                                float(row[5].replace(',', '.'))
                            ]
                            print("Inserindo " + row[1])
                            statement.cursor().execute("""
                                    INSERT INTO CONTABILIDADE (
                                        DATA,
                                        REG_ANS,
                                        DESCRICAO,
                                        CD_CONTA_CONTABIL,
                                        VL_SALDO_INICIAL ,
                                        VL_SALDO_FINAL
                                    ) VALUES (%s, %s, %s, %s, %s, %s)
                                """, rows)
                            statement.commit()

    def deleteContability(self):
        statement = self.mysql.create()
        statement.cursor().execute("""
            DELETE FROM CONTABILIDADE WHERE id > 0
        """)
        statement.commit()

    def selectExpensesFilterByDescription(self,description):
        statement = self.mysql.create()
        execute_statement = statement.cursor("""
            SELECT * FROM CONTABILIDADE WHERE DESCRICAO = %s> 0 LIMIT 10
        """,description)
        print("Busca relizada filtrada por: "+description)
        result = execute_statement
        if result.with_rows:
            for row in execute_statement.fetchall():
                print(row)
        else:
            print("Nenhum resultado foi encontrado")

    def selectBiggerExpensesLastYear(self):
        statement = self.mysql.create()
        print("Aqui esta as 10 maiores operadoras")
        execute_statement = statement.cursor("""
            SELECT 
                REG_ANS, 
                DESCRICAO, 
                SUM(VL_SALDO_INICIAL - VL_SALDO_FINAL) AS total_despesa
            FROM 
                CONTABILIDADE
            WHERE 
                YEAR(DATA) = YEAR(CURDATE()) - 1
            ORDER BY 
                total_despesa DESC
            LIMIT 10;
        """)
        result = execute_statement
        if result.with_rows:
            for row in result.fetchall():
                print(row)
        else:
            print("Nenhum resultado foi encontrado")