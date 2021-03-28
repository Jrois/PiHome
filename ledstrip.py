import RPi.GPIO as GPIO
from time import sleep
from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from signal import pause


class LEDstrip:
    def __init__(self, r, g, b, ww, cw):
        # set up pwm pins
        factory = PiGPIOFactory()
        self.red = PWMLED(r, pin_factory=factory)
        self.green = PWMLED(g, pin_factory=factory)
        self.blue = PWMLED(b, pin_factory=factory)
        self.warm = PWMLED(ww, pin_factory=factory)
        self.cool = PWMLED(cw, pin_factory=factory)

        # initialize state vector
        self.i = 5
        self.states = [0, 0, 0, 0, 0, 0]
        self.states[self.i] = 1

        # pwm value
        self.val = 0.5

    def state_up(self):
        if self.i < 5:
            self.i += 1
        else:
            self.i = 0
        self.update_state()
        self.all_off()
        self.set_strip()

    def state_down(self):
        if self.i > 0:
            self.i -= 1
        else:
            self.i = 5
        self.update_state()
        self.all_off()
        self.set_strip()

    def update_state(self):
        self.states = [0, 0, 0, 0, 0, 0]
        self.states[self.i] = 1

    def set_strip(self):
        # [r, g, b, ww, cw, wwcww] = states
        if self.states[0] == 1:
            self.red.value = self.val
        if self.states[1] == 1:
            self.green.value = self.val
        if self.states[2] == 1:
            self.blue.value = self.val
        if self.states[3] == 1:
            self.warm.value = self.val
        if self.states[4] == 1:
            self.cool.value = self.val
        if self.states[5] == 1:
            self.warm.value = self.val
            self.cool.value = self.val

    def all_off(self):
        self.set_strip([1, 1, 1, 1, 1, 0], 0)

    def increment(self):
        if self.val < 0.9:
            self.val += 0.05
        self.set_strip()

    def decrement(self):
        if self.val > 0.1:
            self.val -= 0.05
        self.set_strip()
