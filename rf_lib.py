import RPi.GPIO as GPIO


def init_rf(A, B, C, D):
    """
    set up rf reciever
    """
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(A, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(B, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(D, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def buttons_pressed(buttons, A, B, C, D):
    buttons = [0, 0, 0, 0]
    if GPIO.input(A):
        buttons[0] = 1
    if GPIO.input(B):
        buttons[1] = 1
    if GPIO.input(C):
        buttons[2] = 1
    if GPIO.input(D):
        buttons[3] = 1
    print(buttons)
    return buttons
