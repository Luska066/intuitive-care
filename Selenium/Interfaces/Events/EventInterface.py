from abc import ABC,abstractmethod

from Selenium.Interfaces.ExecuteScrapping import ExecuteScrapping


class EventInterface(ABC):
    event: ExecuteScrapping = None

    def __init__(self):
        self.event = ExecuteScrapping()

