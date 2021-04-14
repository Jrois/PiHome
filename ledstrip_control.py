from rf_lib import *
from ledstrip_lib import *
import time
import threading

# pin definitions (BCM)
[A, B, C, D] = [26, 19, 13, 6]              # button input pins
[r, g, b, ww, cw] = [2, 3, 4, 14, 15]       # pwm led output pins

buttons = [0, 0, 0, 0]

init_rf(A, B, C, D)
button_listener = threading.Timer(0.1, buttons_pressed, args=(buttons, A, B, C, D))
button_listener.daemon = True
button_listener.start()

while True:
    print(buttons)
    time.sleep(1)

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
