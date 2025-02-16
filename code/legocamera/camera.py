# The core camera itself. The LegoCamera is the class used in the main program.

from __future__ import annotations

from datetime import datetime
from enum import Enum
import libcamera
import os
from pathlib import Path
from picamera2 import Picamera2, Preview
import time

from settings import AutofocusSetting
from widgets import Gallery, Viewfinder

class Picam2Configuration(Enum):
    """Builds a Picamera2 configuration dict from one of three options."""

    def custom_config(picam2: Picamera2, **kwargs) -> dict:
        raise NotImplementedError('Picam2Configuration.custom is not yet implemented.')

    def preview_config(picam2: LegoCamera) -> dict:
        return picam2.create_preview_configuration(transform=picam2.rotation_transform)

    def still_config(picam2: LegoCamera) -> dict:
        return picam2.create_still_configuration(transform=picam2.rotation_transform)

    def video_config(picam2: LegoCamera) -> dict:
        return picam2.create_video_configuration(transform=picam2.rotation_transform)

    preview = preview_config
    still = still_config
    video = video_config

class LegoCamera(Picamera2):
    def __init__(self, camera_config: Picam2Configuration = Picam2Configuration.still, gallery_path: Path = Path('gallery'), autofocus_setting: AutofocusSetting = AutofocusSetting.single_shot):
        """Creates a camera object with extra settings."""

        # TODO find a working way to rotate the image by 90/270 degrees
        self.rotation_transform: libcamera.Transform = libcamera.Transform(rotation=180)  # libcamera.Transform(hflip = True, vflip = True)

        self.autofocus_setting: AutofocusSetting = autofocus_setting
        self.gallery_path: Path = Path(gallery_path)

        super().__init__()
        print()  # Print a blank line after Picamera2() construction messages

        print('Configuring camera...')
        self.camera_config: dict = camera_config(self)
        
        # self.preview_config: dict = self.create_preview_configuration()
        self.preview_config: dict = Picam2Configuration.preview(self)
        self.still_config: dict = Picam2Configuration.still(self)  # self.create_still_configuration()

        self.configure(self.preview_config)

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
        
        self.configure(self.preview_config)
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
        
        self.configure(self.still_config)

        now: datetime.Datetime = datetime.now().strftime('%Y-%m-%d %X').replace(':', '-')
        photo_path: str = f'{self.gallery_path}/{file_name.replace("[datetime]", str(now))}'

        print('Taking a picture...')
        self.start()

        # If autofocus is enabled (not AutofocusSetting.off), wait for autofocus to lock before taking the photo
        if self.autofocus_setting != AutofocusSetting.off:
            print('Autofocussing...')
            autofocus_success: bool = self.autofocus_cycle(wait=False)
            self.wait(autofocus_success, timeout=2)

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
