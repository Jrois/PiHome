from wake_time_lib import *
import time

while True:
    dt = 5
    wt = [16, 15]
    print(wake_light_value(wt, dt))
    time.sleep(1)