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

    while True:
        command = input("Enter command (ON/OFF/EXIT): ").strip().upper()
        if command in ["ON", "OFF"]:
            arduino.write((command + '\n').encode())
            # Read response from Arduino
            response = arduino.readline().decode().strip()
            if response:
                print("Arduino:", response)
        elif command == "EXIT":
            print("Exiting program.")
            break
        else:
            print("Invalid command. Please enter 'ON', 'OFF', or 'EXIT'.")

    arduino.close()

if __name__ == "__main__":
    main()
