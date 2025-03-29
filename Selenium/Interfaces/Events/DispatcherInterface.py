from abc import ABC,abstractmethod

from Selenium.Services.Handler import Handler


class DispatcherInterface(ABC):
    event = {}
    def notify(self): pass
    def register(self,name,event: Handler): pass
    def unregister(self,name): pass
    def unregisterAll(self ):pass
