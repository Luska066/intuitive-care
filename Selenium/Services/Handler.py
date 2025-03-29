# Libs
import sys
import os
from time import sleep

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from Selenium.Enums.DirectoryEnum import DirectoryEnum

# Interface
from Selenium.Interfaces.ExecuteScrapping import ExecuteScrapping


class ServiceHandler(ExecuteScrapping):
    def execute(self):
