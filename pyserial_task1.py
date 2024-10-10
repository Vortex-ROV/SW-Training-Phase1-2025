import serial
import serial.tools.list_ports

def find_arduino_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if "Arduino" in port.description:
            return port.device
    return None

def control_led():
    arduino_port = find_arduino_port()
    if arduino_port is None:
        print("Arduino not exist.")
        return

    with serial.Serial(arduino_port, 9600, timeout=1) as ser:
        while True:
            command = input("Enter 'on' or 'off' to control LED ").strip().lower()

            if command in ['on', 'off']:
                ser.write(f"{command}\n".encode())
                response = ser.readline().decode('utf-8').strip()
                print(f"Arduino response: {response}")
            else:
                print("Invalid option ")

if __name__ == "__main__":
    control_led()
