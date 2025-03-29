from abc import ABC,abstractmethod

from Selenium.Interfaces.Events.EventInterface import EventInterface
from Selenium.Interfaces.ExecuteScrapping import ExecuteScrapping
from Selenium.Services.Events.EventClass import EventClass


class HandlerInterface(ABC):
    event: EventClass  = None
    @abstractmethod
    def handle(self): pass