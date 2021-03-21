import RPi.GPIO as GPIO
from time import sleep
#set up rf reciever
GPIO.setmode(GPIO.BCM)
A = 26
B = 19
C = 13
D = 6
GPIO.setup(A, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(B, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(D, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    print([GPIO.input(A), GPIO.input(B), GPIO.input(C), GPIO.input(D)])
    sleep(0.25)

