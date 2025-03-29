from abc import ABC, abstractmethod

class EventInterface(ABC):
    @abstractmethod
    def run(self): pass
