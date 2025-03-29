from abc import ABC,abstractmethod

class ExecuteScrapping(ABC):
    @abstractmethod
    def execute(self):
        pass