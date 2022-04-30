let i = 0
let red = 0
basic.forever(function () {
    i += 1
    red = 511 * (1 + Math.sin(i / 10))
    pins.analogWritePin(AnalogPin.P0, red)
    pins.analogWritePin(AnalogPin.P1, 0)
    pins.analogWritePin(AnalogPin.P2, 1023 - red)
    control.waitMicros(0.001 * 1000000)
})
