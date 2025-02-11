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
