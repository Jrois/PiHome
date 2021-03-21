from time import localtime, strftime
from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime, timedelta, time

#set up pwm leds
factory = PiGPIOFactory()
warm = PWMLED(14, pin_factory=factory)

# time light
t = datetime.now()
wake_up_time = time(18, 00)
dt = timedelta(minutes=32)

print(t == wake_up_time - dt)
# if H == wake_up_time[0] and M > wake_up_time[1]-30:


