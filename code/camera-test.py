# Example of saving a picture with picamera2
# Copied from section 2.3/page 7 of the picamera2 library manual (https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf)

from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL)
picam2.start()
time.sleep(2)
picam2.capture_file("test.jpg")
