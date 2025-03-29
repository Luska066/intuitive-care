import os

from enum import Enum

class DirectoryEnum(Enum):
    ZIP = os.getcwd()+'/Downloads/ZIP'
    PDF = os.getcwd()+'/Downloads/PDF'