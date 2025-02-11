# Use DRM/KMS to display a preview window. This is the "natural choice" when running on Raspberry Pi OS Lite.
# Copied from section 3.2.2 (page 11) of the picamera2 library manual (https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf)
from picamera2 import Picamera2, Preview

picam2 = Picamera2()
picam2.start_preview(Preview.DRM)
