# Services
from argparse import Action

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

# Options
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Driverrs
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium import webdriver

from Selenium.Actions.CompactFilesPDF import CompactFilesPDF
from Selenium.Actions.DownloadAnexos import DownloadAnexos
from Selenium.Enums.DirectoryEnum import DirectoryEnum
from Selenium.Enums.WebDriversEnum import WebDriversEnum


class SeleniumFactory:
    driverManager = ChromeDriverManager()
    compactService = CompactFilesPDF()
    downloadService = None
    options = None
    service = ChromeService(ChromeDriverManager().install())

    def __init__(self):
        self.defineDriver()

    def defineDriver(self, typeDriver: WebDriversEnum = WebDriversEnum.Chrome):
        match typeDriver:
            case WebDriversEnum.Chrome:
                self.defineChromeConfig()
            case WebDriversEnum.Firefox:
                self.defineChromeConfig()
            case _:
                self.defineChromeConfig()

    def defineChromeConfig(self):
        options = ChromeOptions()
        options.add_argument('--headless')
        options.add_experimental_option("prefs", {
            "download.default_directory": DirectoryEnum.PDF.value,
            "download.prompt_for_download": False,
            "safebrowsing.enabled": True,
            "download.directory_upgrade": True,
            "profile.default_content_settings.popups": 0
        })
        options.add_argument("--disable-popup-blocking")
        self.driverManager = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    def defineFirefoxConfig(self):
        options = FirefoxOptions()
        options.add_argument('--headless')
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.dir", DirectoryEnum.PDF.value)
        options.set_preference("browser.download.useDownloadDir", True)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
        options.set_preference("pdfjs.disabled", True)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("browser.download.panel.shown", False)
        options.set_preference("browser.safebrowsing.enabled", True)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk",
                               "application/pdf,application/octet-stream,application/x-winzip,application/x-zip-compressed,application/zip,multipart/x-zip")
        options.set_preference("dom.popup_blocked", True)
        self.driverManager = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )

    def manufacture(self,Action):
        print("Construindo Fábrica")
        self.downloadService = Action(self.driverManager)

    def deleteFactory(self):
        print("Destruindo Fábrica")
        self.downloadService = None

    def download(self):
        self.downloadService.execute()

    def compactPDFInZip(self):
        self.compactService.execute()
