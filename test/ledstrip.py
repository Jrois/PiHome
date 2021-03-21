import RPi.GPIO as GPIO
from time import sleep
import gpiozero
from gpiozero.pins.pigpio import PiGPIOFactory
from signal import pause

factory = PiGPIOFactory()

b = gpiozero.PWMLED(2, pin_factory=factory)
r = gpiozero.PWMLED(3, pin_factory=factory)
g = gpiozero.PWMLED(4, pin_factory=factory)
ww = gpiozero.PWMLED(14, pin_factory=factory)
cw = gpiozero.PWMLED(15, pin_factory=factory)

b.value = 0
r.value = 0
g.value = 0
ww.value = 0
cw.value = 0


#while True:
#    val = int(input('value to change' ))
#    k += val
#    pi.set_PWM_dutycycle(b, k)
    