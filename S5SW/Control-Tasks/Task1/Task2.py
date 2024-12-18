import serial
import serial.tools.list_ports
import time

def find_arduino_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if "Arduino" in port.description or "CH340" in port.description:
            return port.device
    raise Exception("Arduino not found. Please check the connection.")

def main():
    try:
        arduino_port = find_arduino_port()
        print(f"Arduino found on port: {arduino_port}")
        with serial.Serial(arduino_port, 9600, timeout=1) as arduino:
            time.sleep(2)  # Wait for Arduino to reset
            print("Connected to Arduino.")

            while True:
                command = input("Enter '1' to turn ON the LED, '0' to turn it OFF, or 'q' to quit: ").strip()
                if command == 'q':
                    print("Exiting...")
                    break
                elif command in ['1', '0']:
                    arduino.write(command.encode()) 
                    response = arduino.readline().decode().strip() 
                    print(f"Arduino response: {response}")
                else:
                    print("Invalid input. Please enter '1', '0', or 'q'.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
