from enum import Enum

from picamera2 import Picamera2

class CameraMode(Enum):
    """Defines whether camera exposure settings are set automatically or manually."""
    auto = 0
    manual = 1

class EnabledDisabledSetting(Enum):
    enabled = True
    disabled = False

class AutofocusSetting(Enum):
    single_shot = 0
    continuous = 1

class Picam2Configuration(Enum):
    """Builds a Picamera2 configuration dict from one of three options."""

    def custom_config(picam2: Picamera2, **kwargs) -> dict:
        raise NotImplementedError('Picam2Configuration.custom is not yet implemented.')

    def preview_config(picam2: Picamera2) -> dict:
        return picam2.create_preview_configuration()

    def still_config(picam2: Picamera2) -> dict:
        return picam2.create_still_configuration()

    def video_config(picam2: Picamera2) -> dict:
        return picam2.create_video_configuration()

    preview = preview_config
    still = still_config
    video = video_config
