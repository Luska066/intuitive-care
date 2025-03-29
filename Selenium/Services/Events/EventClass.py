from Selenium.Interfaces.Events.EventInterface import EventInterface

class EventClass(EventInterface):
    event = None
    def __init__(self,event):
        self.event = event

    def run(self):
        self.event.execute()