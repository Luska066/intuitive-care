from time import sleep

from Selenium.Actions.DownloadAnexos import DownloadAnexos
from Selenium.Actions.ExtractPdfToCsv import ExtractPdfToCsv
from Selenium.Services.Dispatcher import Dispatcher
from Selenium.Services.Events.EventClass import EventClass
from Selenium.Services.Events.WebScrapping.ScrappingAccountDemonstration import ScrappingAccountDemonstration
from Selenium.Services.Events.WebScrapping.ScrappingActiveOperators import ScrappingActiveOperators
from Selenium.Services.Events.WebScrapping.ScrappingEvent import ScrappingEvent
from Selenium.Enums.DirectoryEnum import DirectoryEnum
from Selenium.Enums.WebDriversEnum import WebDriversEnum
from Selenium.Factory.SeleniumFactory import SeleniumFactory
from Selenium.Services.Handler import Handler

def selectDriverOption(option,factory):
    match int(opcao):
        case 1:
            print("Executando Chrome")
        case 2:
            print("Executando Firefox")
            factory.defineDriver(WebDriversEnum.Firefox)

print("Iniciando Automação")
print("Automação usando Selenium")

print("")
print("-----------------------------------------")
print("Nos iremos baixar o anexo I e anexo II do site:")
print(DownloadAnexos.url)
print("E compactaremos em arquivo ZIP após o download")
print("-----------------------------------------")
print("")

print("")
print("-----------------------------------------")
print("Os arquivos PDF estarão salvos no diretório : "+ DirectoryEnum.PDF.value)
print("O arquivo ZIP estará salvos no diretório : "+ DirectoryEnum.ZIP.value)
print("-----------------------------------------")
print("")

print("-----------------------------------------")
print("Selecione qual web driver você quer:")
print("Por padrão usaremos o Chrome")
print("")
print("1 - Chrome")
print("2 - Firefox")
print("")
print("-----------------------------------------")

print("")
opcao = input("Digite a opção: ")

factory = SeleniumFactory()
dispatcherEvent = Dispatcher()

selectDriverOption(opcao,factory)

dispatcherEvent.register(
    "downloadAnexo",
    Handler(ScrappingEvent(factory))
)
dispatcherEvent.notify()
dispatcherEvent.unregisterAll()


dispatcherEvent.register(
    "ExtrairTabela",
    Handler(EventClass(ExtractPdfToCsv()))
)
dispatcherEvent.notify()
dispatcherEvent.unregisterAll()


factory = SeleniumFactory()
selectDriverOption(opcao,factory)

dispatcherEvent.register(
    "DownloadAccountDemonstration",
    Handler(ScrappingAccountDemonstration(factory))
)
dispatcherEvent.notify()
dispatcherEvent.unregisterAll()

factory = SeleniumFactory()
selectDriverOption(opcao,factory)
dispatcherEvent.register(
    "downloadAnexo",
    Handler(ScrappingActiveOperators(factory))
)
dispatcherEvent.notify()
dispatcherEvent.unregisterAll()

