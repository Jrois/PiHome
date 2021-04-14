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


def dimUp(ledstrip, event):
    while True:
        event.wait()
        ledstrip.dim_up()
        ledstrip.set_strip(ledstrip.state())
        print(ledstrip.val)
        time.sleep(0.25)
        event.clear()


def dimDown(ledstrip, event):
    while True:
        event.wait()
        ledstrip.dim_down()
        ledstrip.set_strip(ledstrip.state())
        print(ledstrip.val)
        time.sleep(0.25)
        event.clear()


dimUpThread = threading.Thread(target=dimUp, args=(ledstrip, dimUpEvent))
dimUpThread.daemon = True
dimDownThread = threading.Thread(target=dimDown, args=(ledstrip, dimDownEvent))
dimDownThread.daemon = True

dimUpThread.start()
dimDownThread.start()


ledstrip.all_off()
ledstrip.set_strip(ledstrip.state())
print(ledstrip.state(), ledstrip.val)
while True:
    if buttons == [1, 0, 0, 0]:
        dimUpEvent.set()
    if buttons == [0, 1, 0, 0]:
        dimDownEvent.set()

# s = State()
# val = 0.5
# all_off()
# wake_up_time = [7, 30]
# while True:
#     # switch between states
#     if on and buttons_pressed()==[0,0,1,0]:
#         s.up()
#         all_off()
#         set_strip(s.state(),val)
#         sleep(0.5)
#     if on and buttons_pressed()==[0,0,0,1]:
#         s.down()
#         all_off()
#         set_strip(s.state(),val)
#         sleep(0.5)
#
#     # turn on/off
#     if not on and buttons_pressed()==[1,1,0,0]:
#         on = True
#         set_strip(s.state(),val)
#         sleep(0.5)
#     if on and buttons_pressed()==[1,1,0,0]:
#         on = False
#         set_strip(s.state(),0)
#         sleep(0.5)
#
#     # dimming
#     if on and buttons_pressed()==[1,0,0,0]:
#         if val < 0.9:
#             val += 0.05
#         set_strip(s.state(),val)
#         sleep(0.25)
#     if on and buttons_pressed()==[0,1,0,0]:
#         if val > 0.1:
#             val -= 0.05
#         set_strip(s.state(),val)
#         sleep(0.25)
