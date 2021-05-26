from rf_lib import *
from ledstrip_lib import *
from wake_time_lib import *
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
wakeLightEvent = threading.Event()


def dim_up(ledstrip, event):
    while True:
        event.wait()
        ledstrip.dim_up()
        ledstrip.set_strip(ledstrip.state())
        print(ledstrip.val)
        time.sleep(0.2)
        event.clear()


def dim_down(ledstrip, event):
    while True:
        event.wait()
        ledstrip.dim_down()
        ledstrip.set_strip(ledstrip.state())
        print(ledstrip.val)
        time.sleep(0.2)
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


def state_up(ledstrip, event):
    while True:
        event.wait()
        ledstrip.state_up()
        ledstrip.set_strip(ledstrip.state())
        time.sleep(0.5)
        event.clear()


def state_down(ledstrip, event):
    while True:
        event.wait()
        ledstrip.state_down()
        ledstrip.set_strip(ledstrip.state())
        time.sleep(0.5)
        event.clear()


def wake_light(ledstrip, event, wake_time, wake_period):
    while True:
        event.wait()
        ledstrip.wakeLightMode = True
        ledstrip.blink(1, 0.1)
        while ledstrip.wakeLightMode:
            val = wake_light_value(wake_time, wake_period)
            print(val)
            if val:
                ledstrip.set_strip([0, 0, 0, 0, 0, val])
                print(f'val{val} set')
                time.sleep(1)
            elif val > 1:
                ledstrip.wakeLightMode = False
                event.clear()

def logger(buttons, ledstrip):
    while True:
        print(f"buttons:{buttons}\tI/O:{ledstrip.on}\tval:{ledstrip.val}\tstate:{ledstrip.i}\twake mode:{ledstrip.wakeLightMode}")
        time.sleep(0.1)


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

wake_time = [15, 52]
wake_period = 2
wakeLightThread = threading.Thread(target=wake_light, args=(ledstrip, wakeLightEvent, wake_time, wake_period))
wakeLightThread.daemon = True
wakeLightThread.start()

logger = threading.Thread(target=logger, args=(buttons, ledstrip))
logger.daemon = True
logger.start()


ledstrip.all_off()
while True:
    if buttons == [1, 1, 0, 0]:
        IOEvent.set()
    if ledstrip.on:
        if buttons == [1, 0, 0, 0]:
            dimUpEvent.set()
        if buttons == [0, 1, 0, 0]:
            dimDownEvent.set()
        if buttons == [0, 0, 1, 0]:
            stateUpEvent.set()
        if buttons == [0, 0, 0, 1]:
            stateDownEvent.set()
        if not ledstrip.wakeLightMode and buttons == [0, 0, 1, 1]:
            wakeLightEvent.set()
            time.sleep(0.5)
        if ledstrip.wakeLightMode and buttons == [0, 0, 1, 1]:
            ledstrip.wakeLightMode = False
            ledstrip.blink(2, 0.1)
