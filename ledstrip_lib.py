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
        self.val = 0.7

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
        states[self.i] = self.val
        return states

    def set_strip(self, states):
        # [r, g, b, ww, cw, wwcww] = states
        if state[5] == 0:
            self.red.value = self.state[0]
            self.green.value = self.state[1]
            self.blue.value = self.state[2]
            self.warm.value = self.state[3]
            self.cool.value = self.state[4]
        else:
            self.warm.value = self.state[5]
            self.cool.value = self.state[5]
        
    def all_off(self):
        self.set_strip([0, 0, 0, 0, 0, 0])

    def dim_up(self):
        if self.val < 0.95:
            self.val += 0.05

    def dim_down(self):
        if self.val > 0.1:
            self.val -= 0.05

