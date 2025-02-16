# The core camera itself. The LegoCamera is the class used in the main program.

from displays import Gallery, Viewfinder
from enum import Enum

class LegoCamera:
    def __init__(self):
        pass

class CameraDisplay(Enum):
    gallery = Gallery,
    viewfinder = Viewfinder
