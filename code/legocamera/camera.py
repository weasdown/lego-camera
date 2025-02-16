# The core camera itself. The LegoCamera is the class used in the main program.

from widgets import Gallery, Viewfinder
from enum import Enum

class LegoCamera:
    def __init__(self):
        pass

class CameraDisplay(Enum):
    """
    Defines which window is shown to the user.
    
    Either the viewfinder for taking a picture, or gallery for reviewing previous pictures.
    """
    gallery = Gallery
    viewfinder = Viewfinder
