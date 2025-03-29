from datetime import datetime

# Libs
import sys
import os
import zipfile

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from Selenium.Enums.DirectoryEnum import DirectoryEnum

# Interface
from Selenium.Interfaces.ExecuteScrapping import ExecuteScrapping


class DownloadAccountingDemonstrationEvent(ExecuteScrapping):
    url = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"
    action = None
    driver = None
    limit_data = 2
    year_now = datetime.now().year
    directory_pattern = DirectoryEnum.PDF.value + "/AccountingDemonstration"

    def __init__(self, WebDriver: webdriver):
        self.driver = WebDriver
        pass

    def execute(self):
        self.driver.get(self.url)
        print("Iniciando Download...")
        self.searchTwoYearsLater("a")
        print("Download Finalizado...")
        self.driver.quit()

    def searchTwoYearsLater(self, text):
        years = {}
        index = 1
        components = self.driver.find_elements(By.TAG_NAME, text)
        for component in components:
            if len(years) < self.limit_data:
                component_name = str(component.text).replace("/", "")
                if component_name == str(self.year_now):
                    years[component.text] = component.get_attribute("href")
                if component_name == str(self.year_now - 1) or component_name == str(self.year_now - 2):
                    years[component.text] = component.get_attribute("href")
            index += 1

        for year in years:
            self.download(years[year], text, year)

        for year in years:
            self.extractZIP(year)

    def extractZIP(self,year):
        for root, dirs, files in os.walk(self.directory_pattern + "/" + year):
            for file in files:
                if file.endswith('.zip'):
                    zip_file_path = os.path.join(root, file)
                    extract_to_dir = os.path.join(root, "csv/")

                    if not os.path.exists(extract_to_dir):
                        os.makedirs(extract_to_dir)

                    with zipfile.ZipFile(str(zip_file_path), 'r') as zip_ref:
                        zip_ref.extractall(str(extract_to_dir))

    def download(self, url, text, year):
        self.driver.get(url)
        files = self.driver.find_elements(By.TAG_NAME, text)
        for file in files:
            if not os.path.exists(self.directory_pattern + "/" + year):
                os.makedirs(self.directory_pattern + "/" + year)
            href = file.get_attribute('href')
            print(href)
            file_name = file.text

            res = requests.get(href)
            if res.status_code != 200:
                print("Erro ao realizar download do arquivo.")
                sys.exit()

            if res.status_code == 200 or res.status_code == 201:
                print("Arquivo baixado com sucesso.")
                if file_name.endswith(".zip"):
                    print("Salvando o arquivo : " + file_name)
                    with open(os.path.join(self.directory_pattern + "/" + year, file_name), 'wb') as fileYear:
                        fileYear.write(res.content)