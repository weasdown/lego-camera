# Handles the camera's sound

from gpiozero import Buzzer
import legocamera.gpiozero_patch

class Sound:
    def __init__(self, buzzer_pin: int = 17):
        self.buzzer_pin: int = buzzer_pin
        self.buzzer: Buzzer = Buzzer(self.buzzer_pin)

    def beep():
        raise NotImplementedError('Sound.beep() is not yet implemented.')

    def double_beep():
        raise NotImplementedError('Sound.double_beep() is not yet implemented.')

if __name__ == '__main__':
    print('Running sound.py')
    legocamera.gpiozero_patch.patch_gpiozero()
    sound = Sound()
