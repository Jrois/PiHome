from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
import RPi.GPIO as GPIO
from time import sleep, localtime, strftime

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

#set up pwm leds
factory = PiGPIOFactory()
blue = PWMLED(2, pin_factory=factory)
red = PWMLED(3, pin_factory=factory)
green = PWMLED(4, pin_factory=factory)
warm = PWMLED(14, pin_factory=factory)
cool = PWMLED(15, pin_factory=factory)

b = 0.5
r = 0.5
g = 0.5
ww = 0.5
cw = 0.5
on = False
            
class State:
    def __init__(self):
        self.i = 5
    def up(self):
        if self.i<5:
            self.i += 1
        else:
            self.i = 0
    def down(self):
        if self.i>0:
            self.i -= 1
        else:
            self.i = 5
    def state(self):
        states = [0,0,0,0,0,0]
        states[self.i] = 1
        return states
    
def set_strip(states, val):
    # [r, g, b, ww, cw, wwcww] = states
    if states[5] == 1:
        warm.value = val
        cool.value = val
    if states[0] == 1:
        red.value = val
    if states[1] == 1:
        green.value = val
    if states[2] == 1:
        blue.value = val
    if states[3] == 1: 
        warm.value = val
    if states[4] == 1:
        cool.value = val

def all_off():
    set_strip([1,1,1,1,1,0],0)

def buttons_pressed():
    buttons = 0
    if any([GPIO.input(A), GPIO.input(B), GPIO.input(C), GPIO.input(D)]):
        buttons = [0, 0, 0, 0]
        if GPIO.input(A):
            buttons[0] = 1
        else:
            buttons[0] = 0
        if GPIO.input(B):
            buttons[1] = 1
        else:
            buttons[1] = 0
        if GPIO.input(C):
            buttons[2] = 1
        else:
            buttons[2] = 0
        if GPIO.input(D):
            buttons[3] = 1
        else:
            buttons[3] = 0
    return buttons

s = State()
val = 0.5
all_off()
wake_up_time = [7, 30]
while True:
    # switch between states
    if on and buttons_pressed()==[0,0,1,0]:
        s.up()
        all_off()
        set_strip(s.state(),val)
        sleep(0.5)
    if on and buttons_pressed()==[0,0,0,1]:
        s.down()
        all_off()
        set_strip(s.state(),val)
        sleep(0.5)
    
    # turn on/off
    if not on and buttons_pressed()==[1,1,0,0]:
        on = True
        set_strip(s.state(),val)
        sleep(0.5)
    if on and buttons_pressed()==[1,1,0,0]:
        on = False
        set_strip(s.state(),0)
        sleep(0.5)
    
    # dimming
    if on and buttons_pressed()==[1,0,0,0]:
        if val < 0.9:
            val += 0.05
        set_strip(s.state(),val)
        sleep(0.25)
    if on and buttons_pressed()==[0,1,0,0]:
        if val > 0.1:
            val -= 0.05
        set_strip(s.state(),val)
        sleep(0.25)
    
    # time light
#     t = localtime()
#     H = int(strftime("%H"))
#     M = int(strftime("%M"))
#     if state == [0, 0, 0, 0, 0, 1] and H == wake_up_time[0] and M > wake_up_time[1]-30:
        