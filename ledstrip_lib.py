from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory


def init_pwmleds(r, g, b, ww, cw):
    """
    set up pwm leds
    """
    factory = PiGPIOFactory()
    red = PWMLED(r, pin_factory=factory)
    blue = PWMLED(b, pin_factory=factory)
    green = PWMLED(g, pin_factory=factory)
    warm = PWMLED(ww, pin_factory=factory)
    cool = PWMLED(cw, pin_factory=factory)
    return [red, blue, green, warm, cool]

class State:
    def __init__(self):
        self.i = 5
    def up(self):
        if self.i<5:
            self.i += 1
        else:
            self.i = 0
    def down(self):
        if self.i>0:
            self.i -= 1
        else:
            self.i = 5
    def state(self):
        states = [0,0,0,0,0,0]
        states[self.i] = 1
        return states

def set_strip(states, val):
    # [r, g, b, ww, cw, wwcww] = states
    if states[5] == 1:
        warm.value = val
        cool.value = val
    if states[0] == 1:
        red.value = val
    if states[1] == 1:
        green.value = val
    if states[2] == 1:
        blue.value = val
    if states[3] == 1:
        warm.value = val
    if states[4] == 1:
        cool.value = val

def all_off():
    set_strip([1,1,1,1,1,0],0)