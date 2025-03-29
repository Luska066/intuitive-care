from Selenium.Actions.DownloadAccountingDemonstrationEvent import DownloadAccountingDemonstrationEvent
from Selenium.Actions.DownloadAnexos import DownloadAnexos
from Selenium.Factory.SeleniumFactory import SeleniumFactory
from Selenium.Services.Events.EventClass import EventClass

class ScrappingTestThreeEvent(EventClass):
    def __init__(self, event:SeleniumFactory):
        super().__init__(event)

    def run(self):
        self.event.manufacture(DownloadAccountingDemonstrationEvent)
        self.event.download()






