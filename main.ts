radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 40) {
        let Zeit = 0
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
serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    EmpfangeneDaten = serial.readLine()
    serial.writeLine(EmpfangeneDaten)
    if ("FWD" == EmpfangeneDaten) {
        basic.showLeds(`
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            `)
    }
    if ("RWD" == EmpfangeneDaten) {
        basic.showLeds(`
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            `)
    }
})
let EmpfangeneDaten = ""
let Zeit2 = 0
serial.redirect(
SerialPin.P14,
SerialPin.P0,
BaudRate.BaudRate115200
)
radio.setGroup(1)
basic.forever(function () {
	
})
