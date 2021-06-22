from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import *

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
        self.on = False
        self.wakeLightMode = False

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

    def set_strip(self, states, fac=1):
        # [r, g, b, ww, cw, wwcww] = states
        if states[5] == 0:
            self.red.value = states[0]/fac
            self.green.value = states[1]/fac
            self.blue.value = states[2]/fac
            self.warm.value = states[3]/fac
            self.cool.value = states[4]/fac
        else:
            self.warm.value = states[5]/fac
            self.cool.value = states[5]/fac
            self.red.value = 0
        
    def all_off(self):
        self.set_strip([0, 0, 0, 0, 0, 0])

    def dim_up(self):
        if self.val < 0.95:
            self.val += 0.05

    def dim_down(self):
        if self.val > 0.1:
            self.val -= 0.05

    def blink(self, n, t):
        if self.on:
            for i in range(n):
                self.set_strip(self.state(), 3)
                sleep(t)
                self.set_strip(self.state())
                sleep(t)
        else:
            for i in range(n):
                self.set_strip(self.state())
                sleep(t)
                self.set_strip(self.state(), 3)
                sleep(t)
            self.all_off()
