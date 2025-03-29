import os
import subprocess
from time import sleep

from Queries.Boostrap.BootstrapDataBase import BootstrapDataBase

def is_service_running(service_name):
    try:
        # Verifica se o serviço está em execução
        result = subprocess.run(
            ["docker", "ps", "--filter", f"ancestor={service_name}", "--format", "{{.Names}}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        return bool(result.stdout)
    except subprocess.CalledProcessError:
        return False

def start_docker_service():
    service_name = "mysql-container"
    if not is_service_running(service_name):
        subprocess.run(["docker-compose", "up", "-d"], cwd=os.getcwd(), check=True)
    else:
        print(f"Serviço {service_name} já está rodando.")


start_docker_service()
print("Subindo banco de dados, Aguarde 3 segundos!")
sleep(3)

bootstrap = BootstrapDataBase()
bootstrap.initTables()

bootstrap.runOperators()

print('-'*20)
print("Selecione uma opção")
print("1 - Deseja inserir dados do csv no banco?")
print("2 - Consultar as 10 operadoras com maiores Despesas (EVENTOS/ SINISTROS CONHECIDOS)")
print("3 - Consultar as 10 operadoras com maiores Despesas (AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR)")
print("4 - Consultar as 10 com maiores despesas")
print("0 - Finalizar")
opcao = int(input("Seleciona a opção : "))

while opcao != 0:
    match opcao:
        case 1:
            bootstrap.deleteContability()
            print("Lembrando que isso pode demorar um tempo devido")
            print("ao grande volume de dados")
            sleep(4)
            bootstrap.runContability()
            break
        case 2:
            bootstrap.selectExpensesFilterByDescription("EVENTOS/ SINISTROS CONHECIDOS")
            break
        case 3:
            bootstrap.selectExpensesFilterByDescription("AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR")
            break
        case 4:
            print("ok")
            bootstrap.selectBiggerExpensesLastYear()
            break

    print('-' * 20)
    print("Selecione uma opção")
    print("1 - Deseja inserir dados do csv no banco?")
    print("2 - Consultar as 10 operadoras com maiores Despesas (EVENTOS/ SINISTROS CONHECIDOS)")
    print("3 - Consultar as 10 operadoras com maiores Despesas (AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR)")
    print("4 - Consultar as 10 com maiores despesas")
    print("0 - Finalizar")
    opcao = int(input("Seleciona a opção : "))




