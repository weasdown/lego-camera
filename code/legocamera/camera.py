# The core camera itself. The LegoCamera is the class used in the main program.

from datetime import datetime
from enum import Enum
import os
from pathlib import Path
from picamera2 import Picamera2, Preview
import time

from settings import AutofocusSetting, Picam2Configuration
from widgets import Gallery, Viewfinder

class LegoCamera(Picamera2):
    def __init__(self, camera_config: Picam2Configuration = Picam2Configuration.still, gallery_path: Path = Path('gallery'), autofocus_setting: AutofocusSetting = AutofocusSetting.single_shot):
        """Creates a camera object with extra settings."""

        self.autofocus_setting: AutofocusSetting = autofocus_setting
        self.gallery_path: Path = Path(gallery_path)

        super().__init__()
        print()  # Print a blank line after Picamera2() construction messages

        print('Configuring camera...')
        self.camera_config: dict = camera_config(self)
        print(f'Selected configuration: {self.camera_config}\n')
        self.configure(self.camera_config)
        print('Configuration complete!\n')

    @staticmethod
    def get_camera() -> Picamera2:
        try:
            return Picamera2()
        except IndexError as ie:
            NoCameraException(ie)

    @property
    def metadata(self) -> dict:
        """Gets PiCamera2's metadata dict."""
        return self.capture_metadata()

    def record_video(self) -> None:
        raise NotImplementedError('LegoCamera.record_video() is not yet implemented.')

    def start_standard_preview(self, duration: float = 3) -> None:
        """Wrapper for `Picamera2.start_preview()`."""
        original_config: dict = self.camera_config
        
        self.configure(self.create_preview_configuration())
        print('\nStarting preview\n')
        self.start_preview(Preview.QTGL)
        self.start()
        time.sleep(duration)
        self.stop()
        self.stop_preview()

        self.configure(original_config)  # Reset to original config to avoid side effect.

    def take_picture(self, file_name: str = 'test-[datetime].jpg') -> dict:
        """Capture a single image."""

        old_config: dict = self.camera_config
        
        self.configure(self.create_still_configuration())

        print('Taking a picture...')
        now: datetime.Datetime = datetime.now().strftime('%Y-%m-%d %X').replace(':', '-')
        photo_path: str = f'{self.gallery_path}/{file_name.replace("[datetime]", str(now))}'

        self.start()

        # If autofocus is enabled (not AutofocusSetting.off), wait for autofocus to lock before taking the photo
        if self.autofocus_setting != AutofocusSetting.off:
            autofocus_success: bool = self.autofocus_cycle(wait=False)
            self.wait(autofocus_success)

        metadata: dict = self.capture_file(photo_path)
        self.stop()

        self.configure(old_config)  # Revert to old config to avoid side effect.
        return metadata

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

if __name__ == '__main__':
    lego_cam = LegoCamera(camera_config=Picam2Configuration.still)
    print(f'Current autofocus setting: {lego_cam.autofocus_setting}')

    lego_cam.start_standard_preview()

    metadata: dict = lego_cam.take_picture()

    print(f'\nMetadata:\n{metadata}')
    print(f'\nCamera properties:\n{lego_cam.camera_properties}')
