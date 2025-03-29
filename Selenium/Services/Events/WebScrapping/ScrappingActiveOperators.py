from Selenium.Actions.DownloadAccountingDemonstrationEvent import DownloadAccountingDemonstrationEvent
from Selenium.Actions.DownloadActiveOperators import DownloadActiveOperators
from Selenium.Actions.DownloadAnexos import DownloadAnexos
from Selenium.Factory.SeleniumFactory import SeleniumFactory
from Selenium.Services.Events.EventClass import EventClass

class ScrappingActiveOperators(EventClass):
    def __init__(self, event:SeleniumFactory):
        super().__init__(event)

    def run(self):
        self.event.manufacture(DownloadActiveOperators)
        self.event.download()






