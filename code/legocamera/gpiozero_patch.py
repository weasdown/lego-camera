# Copied from: https://github.com/gpiozero/gpiozero/issues/1166#issuecomment-2306937929

import gpiozero.pins.lgpio
import lgpio

def __patched_init(self, chip=None):
    gpiozero.pins.lgpio.LGPIOFactory.__bases__[0].__init__(self)
    chip = 0
    self._handle = lgpio.gpiochip_open(chip)
    self._chip = chip
    self.pin_class = gpiozero.pins.lgpio.LGPIOPin

def patch_gpiozero():
    gpiozero.pins.lgpio.LGPIOFactory.__init__ = __patched_init
    print('Patched gpiozero')

if __name__ == '__main__':
    patch_gpiozero()
