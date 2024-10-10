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
        print(ser.readline())
