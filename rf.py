import RPi.GPIO as GPIO


class RF_receiver:
    def __init__(self, A, B, C, D):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(A, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(B, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(C, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(D, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def buttons_pressed(self):
        buttons = 0
        if any([GPIO.input(self.A), GPIO.input(self.B), GPIO.input(self.C), GPIO.input(self.D)]):
            buttons = [0, 0, 0, 0]
            if GPIO.input(self.A):
                buttons[0] = 1
            else:
                buttons[0] = 0
            if GPIO.input(self.B):
                buttons[1] = 1
            else:
                buttons[1] = 0
            if GPIO.input(self.C):
                buttons[2] = 1
            else:
                buttons[2] = 0
            if GPIO.input(self.D):
                buttons[3] = 1
            else:
                buttons[3] = 0
        return buttons
