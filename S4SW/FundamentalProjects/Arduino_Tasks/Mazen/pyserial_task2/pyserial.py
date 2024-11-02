import serial
import serial.tools.list_ports
import time

def find_arduino_port():
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if "Arduino" in port.description or "USB Serial Device" in port.description:
            return port.device
    return None

def main():
    port = find_arduino_port()
    if port is None:
        print("Arduino not found. Please check the connection.")
        return

    # Connect to the Arduino
    arduino = serial.Serial(port, 9600, timeout=1)
    time.sleep(2)  # Wait for the connection to initialize

    print("Connected to Arduino on port:", port)
    print("Type 'ON' to turn LED on and 'OFF' to turn it off. Type 'EXIT' to quit.")

    try:
        while True:
            if arduino.in_waiting > 0:                
                # Read response from Arduino
                state = arduino.readline().decode().strip()
                print("button state: " + state)
    except KeyboardInterrupt:
            print("Exiting program.")
    finally:
            arduino.close()

if __name__ == "__main__":
    main()
