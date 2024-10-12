import serial
import serial.tools.list_ports
import time

# Function to find the Arduino port
def find_arduino_port():
    ports = serial.tools.list_ports.comports() #from the pyserial library
    for port in ports:
        if "CH340" in port[1]:  # Look for Arduino in the port description
            return port[0]       #return the device name like (com3)
        else :
            return None
ard_port = find_arduino_port()
if ard_port is None:
    print("Arduino not found. Please connect your Arduino!")
else:
    print(f"Arduino found on port: {ard_port}")  #ardunio found in port :com3
    # Set up serial communication
    ser = serial.Serial(ard_port, 9600, timeout=1)
    time.sleep(3)  

    try:
        while True:
            command = input("Enter '1' to turn ON the LED, '0' to turn OFF the LED, or 'q' to quit: ")
            if command in ['1', '0']:
                ser.write(command.encode())  # Send command to Arduino ,converts the string to bytes.
            elif command == 'q':
                print("Exiting...")
                break
            else:
                print("Invalid input. Please enter 1,0, or q")
    except KeyboardInterrupt:
        print("Exiting due to keyboard interrupt problem.")
    finally:
        ser.close() 
