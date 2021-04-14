import RPi.GPIO as GPIO
import time

def init_rf(A, B, C, D):
    """
    set up rf reciever
    """
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(A, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(B, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(D, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def get_buttons_pressed(buttons, A, B, C, D):
    next_call = time.time()
    while True:
        buttons[0] = 0
        buttons[1] = 0
        buttons[2] = 0
        buttons[3] = 0
        if GPIO.input(A):
            buttons[0] = 1
        if GPIO.input(B):
            buttons[1] = 1
        if GPIO.input(C):
            buttons[2] = 1
        if GPIO.input(D):
            buttons[3] = 1
        next_call = next_call + 0.1
        time.sleep(next_call - time.time())
