import RPi.GPIO as GPIO
from time import sleep

led = 2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)

while True:
    GPIO.output(led, GPIO.HIGH)
    sleep(1)
    GPIO.output(led, GPIO.LOW)
    sleep(1)