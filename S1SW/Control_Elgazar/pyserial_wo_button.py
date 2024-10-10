import serial
import serial.tools.list_ports

ports = list(serial.tools.list_ports.comports())
arduino_port = None
for p in ports:
    if "CH340" in p[1]:
        arduino_port = p[0]

print(arduino_port)
with serial.Serial() as ser:
    ser.baudrate = 9600
    ser.port = arduino_port
    ser.open()
    while True:
        userIn = input("Enter your command:")
        match userIn:
            case "on":
                ser.write(bytes(b"on"))
            case "off":
                ser.write(bytes(b"off"))
            case "q":
                break
            case _:
                print("Invalid input. Try again.")
