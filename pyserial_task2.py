import serial
import serial.tools.list_ports

def find_arduino_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if "Arduino" in port.description:
            return port.device
    return None

def read_button_state():
    arduino_port = find_arduino_port()
    if arduino_port is None:
        print("Arduino not found.")
        return


    ser = serial.Serial(arduino_port, 9600, timeout=1)
    print(f"Connected to {arduino_port}")

    while True:
        if ser.in_waiting > 0:
            button_state = ser.readline().decode('utf-8').strip()
            print(f"Arduino: {button_state}")

if __name__ == "__main__":
    read_button_state()
