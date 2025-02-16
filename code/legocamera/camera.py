# The core camera itself. The LegoCamera is the class used in the main program.

from enum import Enum
from picamera2 import Picamera2, Preview

from .widgets import Gallery, Viewfinder

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
