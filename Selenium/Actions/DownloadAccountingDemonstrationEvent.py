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

class DownloadArchivesTestThree(ExecuteScrapping):
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    action = None
    driver = None

    def __init__(self, WebDriver: webdriver):
        self.driver = WebDriver
        pass

    def downloadArchiveByInnerText(self, text):
        # variáveis
        component = self.driver.find_element(By.LINK_TEXT, text)
        href = component.get_attribute('href')
        file_name = href.split('/')[-1]
        link_to_download = href

        # Baixando o arquivo
        print("")
        print("")
        print("Baixando link: " + link_to_download)
        response = requests.get(link_to_download)
        if response.status_code != 200:
            print("Erro ao realizar download do arquivo.")
            sys.exit()

        if response.status_code == 200 or response.status_code == 201:
            print("Arquivo baixado com sucesso.")
            print("Salvando o arquivo : " + file_name)
            with open(os.path.join(DirectoryEnum.PDF.value, file_name), 'wb') as file:
                file.write(response.content)

    def execute(self):
        self.driver.get(self.url)
        print("Iniciando Download...")
        self.downloadArchiveByInnerText("Anexo I.")
        print("Download Finalizado...")

        sleep(1)
        print("Iniciando Download...")
        self.downloadArchiveByInnerText("Anexo II.")
        print("Download Finalizado...")
        self.driver.quit()
