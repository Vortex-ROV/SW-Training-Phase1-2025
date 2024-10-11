import serial
import serial.tools.list_ports
import time


def find_arduino_port():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if 'CH340' in p.description:
            return p.device
    return None


def main():
    arduino_port = find_arduino_port()
    if arduino_port is None:
        print("Arduino not found. Please check the connection.")
        return

    print(f"Arduino found on port: {arduino_port}")

    try:
        ser = serial.Serial(arduino_port, 9600, timeout=1)
        time.sleep(2)  # Wait for the connection to establish

        print("Monitoring button state. Press Ctrl+C to exit.")
        while True:
            if ser.in_waiting > 0:
                button_state = ser.readline().decode().strip()
                print(f"Button state: {button_state}")
    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    finally:
        if 'ser' in locals():
            ser.close()
            print("Serial connection closed.")


if __name__ == "__main__":
    main()