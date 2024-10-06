import serial.tools.list_ports

# Function to automatically find the Arduino port
ports = serial.tools.list_ports.comports()

arduino_port = None

# Check each available port
for port in ports:
    if "Arduino" in port.description or "CH340" in port.description:  # Detect Arduino
        arduino_port = port.device
        break

if arduino_port is None:
    print("Arduino not found!")
    exit()

print(f"Arduino found on {arduino_port}")

# Set up serial communication
serialInst = serial.Serial()

serialInst.baudrate = 9600
serialInst.port = arduino_port
serialInst.open()

valid_commands = ['ON', 'OFF', 'exit']

while True:
    # Ask for user input
    command = input("Arduino Command (ON/OFF/exit): ").strip()

    # Check if input is valid
    if command.upper() in valid_commands:
        # Send valid command to Arduino
        serialInst.write(command.encode('utf-8'))

        if command.lower() == 'exit':  # Check for exit
            print("Exiting...")
            serialInst.close()  # Properly close the serial port
            break
    else:
        # Handle invalid input
        print("Invalid input! Please enter 'ON', 'OFF', or 'exit'.")
