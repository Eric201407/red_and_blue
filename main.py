i = 0
red = 0

def on_forever():
    global i, red
    i += 1
    red = 511 * (1 + Math.sin(i / 10))
    pins.analog_write_pin(AnalogPin.P0, red)
    pins.analog_write_pin(AnalogPin.P1, 0)
    pins.analog_write_pin(AnalogPin.P2, 1023 - red)
    control.wait_micros(0.001 * 1000000)
basic.forever(on_forever)
