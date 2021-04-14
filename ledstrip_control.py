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
            ledstrip.on = True
        else:
            ledstrip.all_off()
            ledstrip.on = False
        time.sleep(0.5)
        event.clear()


dimUpThread = threading.Thread(target=dim_up, args=(ledstrip, dimUpEvent))
dimUpThread.daemon = True
dimDownThread = threading.Thread(target=dim_down, args=(ledstrip, dimDownEvent))
dimDownThread.daemon = True
IOThread = threading.Thread(target=on_off, args=(ledstrip, IOEvent))
IOThread.daemon = True

dimUpThread.start()
dimDownThread.start()
IOThread.start()

ledstrip.all_off()
while True:
    if buttons == [1, 0, 0, 0]:
        dimUpEvent.set()
    if buttons == [0, 1, 0, 0]:
        dimDownEvent.set()
    if buttons == [1, 1, 0, 0]:
        IOEvent.set()
