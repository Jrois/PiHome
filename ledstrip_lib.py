from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory


class LedStrip:
    def __init__(self, r, g, b, ww, cw):
        self.i = 5
        factory = PiGPIOFactory()
        self.red = PWMLED(r, pin_factory=factory)
        self.blue = PWMLED(b, pin_factory=factory)
        self.green = PWMLED(g, pin_factory=factory)
        self.warm = PWMLED(ww, pin_factory=factory)
        self.cool = PWMLED(cw, pin_factory=factory)

    def state_up(self):
        if self.i < 5:
            self.i += 1
        else:
            self.i = 0

    def state_down(self):
        if self.i > 0:
            self.i -= 1
        else:
            self.i = 5

    def state(self):
        states = [0, 0, 0, 0, 0, 0]
        states[self.i] = 1
        return states

    def set_strip(self, states, val):
        # [r, g, b, ww, cw, wwcww] = states
        if states[5] == 1:
            self.warm.value = val
            self.cool.value = val
        if states[0] == 1:
            self.red.value = val
        if states[1] == 1:
            self.green.value = val
        if states[2] == 1:
            self.blue.value = val
        if states[3] == 1:
            self.warm.value = val
        if states[4] == 1:
            self.cool.value = val

    def all_off(self):
        self.set_strip([1, 1, 1, 1, 1, 0], 0)
