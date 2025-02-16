from enum import Enum

class CameraMode(Enum):
    auto = 0
    manual = 1

class EnabledDisabledSetting(Enum):
    enabled = True
    disabled = False

class AutofocusSetting(EnabledDisabledSetting):
    enabled = super.enabled
    disabled = super.disabled
