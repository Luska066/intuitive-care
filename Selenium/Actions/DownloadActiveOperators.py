from datetime import datetime

from Selenium.Interfaces.ExecuteScrapping import ExecuteScrapping
# Libs
import sys
import os
from time import sleep

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from Selenium.Enums.DirectoryEnum import DirectoryEnum

# Interface
from Selenium.Interfaces.ExecuteScrapping import ExecuteScrapping


class DownloadActiveOperators(ExecuteScrapping):
    url = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/"
    action = None
    driver = None
    directory_pattern = DirectoryEnum.PDF.value + "/ActiveOperators"

    def __init__(self, WebDriver: webdriver):
        self.driver = WebDriver
        pass

    def execute(self):
        self.driver.get(self.url)
        print("Iniciando Download...")
        self.download("a")
        print("Download Finalizado...")
        self.driver.quit()

    def download(self, text):
        components = self.driver.find_elements(By.TAG_NAME, text)
        for component in components:
            if component.text.endswith(".csv"):
                res = requests.get(component.get_attribute("href"))
                if res.status_code != 200:
                    print("Erro ao realizar download do arquivo.")
                    sys.exit()

                if res.status_code == 200 or res.status_code == 201:
                    print("Arquivo baixado com sucesso.")
                    print("Salvando o arquivo : " + component.text)
                    with open(os.path.join(self.directory_pattern, component.text), 'wb') as fileYear:
                        fileYear.write(res.content)