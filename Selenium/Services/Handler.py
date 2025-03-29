# Libs
import sys
import os
from abc import ABC
from time import sleep

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from Selenium.Interfaces.Events.EventInterface import EventInterface
from Selenium.Interfaces.Events.HandlerInterface import HandlerInterface

# Interface
from Selenium.Interfaces.ExecuteScrapping import ExecuteScrapping
from Selenium.Services.Events.EventClass import EventClass


class Handler(HandlerInterface):
    event: EventClass = None

    def __init__(self, event:EventClass):
        self.event = event

    def handle(self):
        self.event.run()

