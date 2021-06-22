from wake_time_lib import *
import time

while True:
    dt = 1
    wt = [21, 23]
    print(wake_light_value(wt, dt))
    time.sleep(1)
