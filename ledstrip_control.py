from time import sleep


# switch between states
def switch_states(strip, rf, on):
    if on and rf.buttons_pressed() == [0, 0, 1, 0]:
        strip.state_up()
        sleep(0.5)

    if on and rf.buttons_pressed() == [0, 0, 0, 1]:
        strip.state_down()
        sleep(0.5)


# turn on/off
def switch_on_off(strip, rf, on):
    if not on and rf.buttons_pressed() == [1, 1, 0, 0]:
        on = True
        strip.set_strip()
        sleep(0.5)

    if on and rf.buttons_pressed() == [1, 1, 0, 0]:
        on = False
        strip.all_off()
        sleep(0.5)


# dimming
def dimming(strip, rf, on):
    if on and rf.buttons_pressed() == [1, 0, 0, 0]:
        strip.increment()
        sleep(0.25)
    if on and rf.buttons_pressed() == [0, 1, 0, 0]:
        strip.decrement()
        sleep(0.25)
