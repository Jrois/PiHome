from time import sleep


# switch between states
def switch_states(strip, rf):
    if strip.on and rf.buttons_pressed() == [0, 0, 1, 0]:
        strip.state_up()
        sleep(0.5)

    if strip.on and rf.buttons_pressed() == [0, 0, 0, 1]:
        strip.state_down()
        sleep(0.5)


# turn on/off
def switch_on_off(strip, rf):
    if not strip.on and rf.buttons_pressed() == [1, 1, 0, 0]:
        print('switch on yeah')
        strip.on = True
        strip.set_strip(strip.state, strip.val)
        sleep(0.5)

    if strip.on and rf.buttons_pressed() == [1, 1, 0, 0]:
        strip.on = False
        strip.all_off()
        sleep(0.5)


# dimming
def dimming(strip, rf):
    if strip.on and rf.buttons_pressed() == [1, 0, 0, 0]:
        strip.increment()
        sleep(0.25)
    if strip.on and rf.buttons_pressed() == [0, 1, 0, 0]:
        strip.decrement()
        sleep(0.25)
