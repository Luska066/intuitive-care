from Selenium.Interfaces.ExecuteScrapping import ExecuteScrapping
from Selenium.Services.Events.EventClass import EventClass


class ScrappingEvent(EventClass):
    def __init__(self, event:ExecuteScrapping):
        super().__init__(event)




