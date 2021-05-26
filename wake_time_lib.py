from datetime import datetime, timedelta

# time light
def wake_light_value(wt, dt):
    """
    return float based on how far in the wake interval the current time is
    :param wt: wake time [hour, minute]
    :param dt: time period in minutes
    :return:
    """
    [h, m] = wt
    wake_time = datetime(1, 1, 1, hour=h, minute=m)
    timeperiod = timedelta(minutes=dt)
    current_time = datetime.now()
    if (wake_time - timeperiod).time() < current_time.time() < wake_time.time():
        return get_light_value(wt, dt)
    elif current_time.time() > wake_time.time():
        return 100
    else:
        return False

def time2integer(time):
    return 60*time.hour + time.minute + time.second/60

def lin_interpol(x, X, Y):
    [x1, x2] = X
    [y1, y2] = Y
    return y1 + ((x - x1)/ (x2 - x1)) * (y2 - y1)

def get_light_value(wt, dt):
    current_time = datetime.now()
    [h, m] = wt
    wake_time = datetime(1, 1, 1, hour=h, minute=m)
    timeperiod = timedelta(minutes=dt)
    return lin_interpol(time2integer(current_time), [time2integer((wake_time-timeperiod).time()), time2integer(wake_time)], [0, 0.95])
