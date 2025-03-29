from Selenium.Actions.DownloadAnexos import DownloadAnexos
from Selenium.Factory.SeleniumFactory import SeleniumFactory
from Selenium.Services.Events.EventClass import EventClass


class ScrappingEvent(EventClass):
    def __init__(self, event:SeleniumFactory):
        super().__init__(event)

    def run(self):
        self.event.manufacture(DownloadAnexos)
        self.event.download()
        self.event.compactPDFInZip()






