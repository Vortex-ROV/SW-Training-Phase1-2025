import serial.tools.list_ports
import serial
import time

# Automatically find the port to which the Arduino is connected
ports = serial.tools.list_ports.comports()
arduino_port = None

for port in ports:
    if "Arduino" in port.description or "CH340" in port.description:  # Check for Arduino-like descriptors
        arduino_port = port.device
        break

if arduino_port is None:
    print("Arduino not found!")
    exit()

print(f"Arduino found on {arduino_port}")

# Set up serial communication
try:
    serialInst = serial.Serial(arduino_port, baudrate=9600, timeout=1)
    time.sleep(2)  # Allow time for the connection to establish
    print("Connected to Arduino successfully!")

except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit()

# Continuously read button state from Arduino
try:
    while True:
        if serialInst.in_waiting > 0:
            # Read data from the serial port
            line = serialInst.readline().decode('utf-8').strip()
            print(f"Button State: {line}")

        time.sleep(0.1)  # To avoid overwhelming the CPU
except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Close the serial connection on exit
    serialInst.close()
