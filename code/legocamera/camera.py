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

class NoCameraException(Exception):
    def __init__(self, index_error: IndexError, from_None: bool = True):            
        # Call the base class constructor with the parameters it needs
        super().__init__('Python did not find a camera attached to this system. Please check you have a camera connected.')

        raise self from None if from_None == True else index_error

def get_camera()->Picamera2:
    try:
        return Picamera2()
    except IndexError as ie:
        NoCameraException(ie)
