def on_received_number(receivedNumber):
    global Zeit2
    if receivedNumber == 40:
        basic.show_leds("""
            . . . # .
                        . # . # .
                        . . # # .
                        . . # . .
                        . . . # .
        """)
        Zeit2 = control.millis()
        serial.write_value("Zeitdifferenz", Zeit2 - Zeit)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global Zeit
    Zeit = control.millis()
    basic.show_leds("""
        . . . . .
                . # # # .
                . # . # .
                . . # # .
                . . . . .
    """)
    radio.send_number(30)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_data_received():
    global EmpfangeneDaten
    EmpfangeneDaten = serial.read_string()
    serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, BaudRate.BAUD_RATE115200)
    serial.write_string(EmpfangeneDaten)
    if "FWD\n" == EmpfangeneDaten:
        basic.show_leds("""
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        """)
    if "RWD\n" == EmpfangeneDaten:
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        """)
    serial.redirect(SerialPin.P14, SerialPin.P0, BaudRate.BAUD_RATE115200)
serial.on_data_received(serial.delimiters(Delimiters.NEW_LINE), on_data_received)

EmpfangeneDaten = ""
Zeit = 0
Zeit2 = 0
serial.redirect(SerialPin.P14, SerialPin.P0, BaudRate.BAUD_RATE115200)
radio.set_group(1)

def on_forever():
    pass
basic.forever(on_forever)
