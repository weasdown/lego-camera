# Handles the camera's sound

from gpiozero import Buzzer
import gpiozero_patch

class Sound:
    def __init__(self, buzzer_pin: int = 17):
        self.buzzer_pin: int = buzzer_pin
        self.buzzer: Buzzer = Buzzer(self.buzzer_pin)

    def beep():
        raise NotImplementedError()

    def double_beep():
        raise NotImplementedError()

if __name__ == '__main__':
    print('Running sound.py')
    gpiozero_patch.patch_gpiozero()
    sound = Sound()
