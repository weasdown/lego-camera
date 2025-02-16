# Custom camera code using picamera2
# Based on examples from the picamera2 library manual (https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf)

import libcamera as lc
from picamera2 import Preview
import time

from legocamera import LegoCamera

picam2 = LegoCamera.get_camera()

# Set camera configuration parameters
config = picam2.create_preview_configuration()
config = picam2.create_still_configuration()
picam2.configure(config)

# See section 5.1.2, page 31 (PDF page 32)
with picam2.controls as controls:
    controls.ExposureTime = 10000
    # controls.AnalogueGain = 1.0
    controls.AfMode = lc.controls.AfModeEnum.Continuous

picam2.start_preview(Preview.QTGL)
picam2.start(show_preview=True)
time.sleep(1)

job = picam2.autofocus_cycle(wait=False)
# Now do some other things, and when you finally want to be sure the autofocus
# cycle is finished:
success = picam2.wait(job)
print(f'Autofocus success? {success}\n')

# Capture and print some properties of the image metadata
metadata = picam2.capture_metadata()
controls = {c: metadata[c] for c in ["ExposureTime", "AnalogueGain", "ColourGains"]}
print(f'Metadata:\n{controls}')
