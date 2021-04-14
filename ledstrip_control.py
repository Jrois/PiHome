from rf_lib import *
from ledstrip_lib import *
import time
import threading

# rf receiver init
[A, B, C, D] = [26, 19, 13, 6]  # button input pins (BCM)
buttons = [0, 0, 0, 0]
init_rf(A, B, C, D)
button_listener = threading.Thread(target=get_buttons_pressed, args=(buttons, A, B, C, D))
button_listener.daemon = True
button_listener.start()

# ledstrip init
[r, g, b, ww, cw] = [2, 3, 4, 14, 15]  # pwm led output pins (BCM)
ledstrip = LedStrip(r, g, b, ww, cw)

# event initialisations
stateUpEvent = threading.Event()
stateDownEvent = threading.Event()
dimUpEvent = threading.Event()
dimDownEvent = threading.Event()
IOEvent = threading.Event()


def dim_up(ledstrip, event):
    while True:
        event.wait()
        ledstrip.dim_up()
        ledstrip.set_strip(ledstrip.state())
        print(ledstrip.val)
        time.sleep(0.25)
        event.clear()


def dim_down(ledstrip, event):
    while True:
        event.wait()
        ledstrip.dim_down()
        ledstrip.set_strip(ledstrip.state())
        print(ledstrip.val)
        time.sleep(0.25)
        event.clear()


def on_off(ledstrip, event):
    while True:
        event.wait()
        if not ledstrip.on:
            ledstrip.set_strip(ledstrip.state())
        else:
            ledstrip.all_off()
        time.sleep(0.5)
        event.clear()

def state_up(ledstrip, event):
    while True:
        event.wait()
        ledstrip.state_up()
        ledstrip.set_strip(ledstrip.state())
        time.sleep(0.5)
        event.clear()

def state_up(ledstrip, event):
    while True:
        event.wait()
        ledstrip.state_down()
        ledstrip.set_strip(ledstrip.state())
        time.sleep(0.5)
        event.clear()


dimUpThread = threading.Thread(target=dim_up, args=(ledstrip, dimUpEvent))
dimUpThread.daemon = True
dimUpThread.start()

dimDownThread = threading.Thread(target=dim_down, args=(ledstrip, dimDownEvent))
dimDownThread.daemon = True
dimDownThread.start()

IOThread = threading.Thread(target=on_off, args=(ledstrip, IOEvent))
IOThread.daemon = True
IOThread.start()

stateUpThread = threading.Thread(target=state_up, args=(ledstrip, stateUpEvent))
stateUpThread.daemon = True
stateUpThread.start()

stateDownThread = threading.Thread(target=state_down, args=(ledstrip, stateDownEvent))
stateDownThread.daemon = True
stateDownThread.start()

ledstrip.all_off()
ledstrip.set_strip(ledstrip.state())
print(ledstrip.state(), ledstrip.val)
while True:
    if buttons == [1, 0, 0, 0]:
        dimUpEvent.set()
    if buttons == [0, 1, 0, 0]:
        dimDownEvent.set()
    if buttons == [1, 1, 0, 0]:
        IOEvent.set()
    if buttons == [0, 0, 1, 0]:
        stateUpEvent.set()
    if buttons == [0, 0, 0, 1]:
        stateUpEvent.set()
