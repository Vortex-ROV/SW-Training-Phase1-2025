import serial.tools.list_ports
import time

def ard():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if 'CH340' in port.description:
            return port.device
    return None

def led():
    ardPort = ard()
    if not ardPort:
        print("Arduino not found!")
        return

    ser = serial.Serial(ardPort, 9600)
    time.sleep(2) 

    while True:
        command = input(" 1: turn ON the LED, 0 : OFF,  q : quit: ")
        if command == 'q':
            break
        elif command in ['1', '0']:
            ser.write(command.encode()) 
        else:
            print("Invalid input!")

    ser.close()

led()
