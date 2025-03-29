import os

from enum import Enum

class DirectoryEnum(Enum):
    PDF = os.getcwd()+'/Selenium/Downloads/PDF'
    CSV = os.getcwd()+'/Selenium/Archives/CSV'
    ZIP = os.getcwd()+'/Selenium/Archives/ZIP'
