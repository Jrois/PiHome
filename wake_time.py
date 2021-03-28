from datetime import datetime, timedelta
from scipy.interpolate import interp1d


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
    else:
        return False


def time2integer(time):
    return 60 * time.hour + time.minute


def get_light_value(wt, dt):
    current_time = datetime.now()
    [h, m] = wt
    wake_time = datetime(1, 1, 1, hour=h, minute=m)
    timeperiod = timedelta(minutes=dt)
    f = interp1d([time2integer((wake_time - timeperiod).time()), time2integer(wake_time)], [0, 1])
    return f(time2integer(current_time))

# dt = 33
# wt = [18, 00]
#
# print(wake_light_value(wt, dt))
