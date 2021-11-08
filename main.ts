radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 40) {
        basic.showLeds(`
            . . . # .
            . # . # .
            . . # # .
            . . # . .
            . . . # .
            `)
        Zeit2 = control.millis()
        serial.writeValue("Zeitdifferenz", Zeit2 - Zeit)
    }
})
input.onButtonPressed(Button.A, function () {
    Zeit = control.millis()
    basic.showLeds(`
        . . . . .
        . # # # .
        . # . # .
        . . # # .
        . . . . .
        `)
    radio.sendNumber(30)
})
serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    basic.showIcon(IconNames.Heart)
})
let Zeit = 0
let Zeit2 = 0
serial.redirect(
SerialPin.P0,
SerialPin.P1,
BaudRate.BaudRate115200
)
radio.setGroup(1)
basic.forever(function () {
	
})
