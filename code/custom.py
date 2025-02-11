# Custom camera code using picamera2
# Based on examples from the picamera2 library manual (https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf)

from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()

# Set camera configuration parameters
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)

# See section 5.1.2, page 31 (PDF page 32)
with picam2.controls as controls:
    controls.ExposureTime = 10000
    controls.AnalogueGain = 1.0
    # print(controls)

picam2.start_preview(Preview.QTGL)
picam2.start()
