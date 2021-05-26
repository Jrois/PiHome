from wake_time_lib import *
import time

while True:
    dt = 2
    wt = [15, 56]
    print(wake_light_value(wt, dt))
    time.sleep(1)