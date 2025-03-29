from abc import ABC,abstractmethod

from Selenium.Interfaces.Events.DispatcherInterface import DispatcherInterface
from Selenium.Services.Handler import Handler


class Dispatcher(DispatcherInterface):
    event = {}

    def notify(self):
        for event in self.event:
            if self.event[event] is not None:
                self.event[event].handle()
        pass

    def register(self,name,event: Handler):
        self.event[name] = event
        pass

    def unregister(self,name):
        del self.event[name]
        pass

    def unregisterAll(self ):
        self.event = {}
        pass