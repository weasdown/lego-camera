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
    off = 0
    single_shot = 1
    continuous = 2
