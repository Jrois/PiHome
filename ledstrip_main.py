from rf import *
from ledstrip import *
from ledstrip_control import *

# set up rf receiver
[A, B, C, D] = [26, 19, 13, 6]  # RF input pin numbers (BCM)
rf = RF_receiver(A, B, C, D)

# set up PWM LEDs
[r, g, b, ww, cw] = [3, 4, 2, 14, 15]  # PWM output pin numbers (BCM)
strip = LEDstrip(r, g, b, ww, cw)

strip.all_off()
wake_up_time = [7, 30]
i = 0
while True:
    switch_states(strip, rf)  # switch between states
    switch_on_off(strip, rf)  # turn on/off
    dimming(strip, rf)  # dimming
#     if i % 10000 == 0:
#         print([rf.buttons_pressed(), strip.on, strip.states])
    i += 1