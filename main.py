radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 40) {
        Zeit2 = timeanddate.dateTime()
        serial.writeValue("Zeitdifferenz", Zeit2 - Zeit)
        basic.showLeds(`
            # # # # .
            # . . # .
            # # # . .
            # . . # .
            # # # # .
            `)
    }
    if (receivedNumber == 50) {
        basic.showLeds(`
            . . # . .
            . # . # .
            . # # # .
            # . . . #
            # . . . #
            `)
    }
})
input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    radio.sendNumber(20)
})
input.onButtonPressed(Button.B, function () {
    Zeit = timeanddate.dateTime()
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    radio.sendNumber(30)
})
let Zeit = ""
let Zeit2 = ""
radio.setGroup(1)
basic.forever(function () {
	
})
