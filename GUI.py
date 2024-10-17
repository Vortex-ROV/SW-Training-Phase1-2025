import tkinter as tk
import serial
import time
import keyboard
import threading

# Initialize serial connection
ser = serial.Serial('COM6', 9600)

# Robot control functions
def move_forward():
    ser.write(b'w')
    update_status("Moving Forward")

def move_backward():
    ser.write(b's')
    update_status("Moving Backward")

def turn_left():
    ser.write(b'd')
    update_status("Turning Left")

def turn_right():
    ser.write(b'a')
    update_status("Turning Right")

def stop():
    ser.write(b'm')
    update_status("Stopped")

def turn_on_laser():
    ser.write(b'u')
    update_status("Laser On")

def turn_off_laser():
    ser.write(b'p')
    update_status("Laser Off")

def update_status(action):
    status_label.config(text=f"Status: {action}")

# Function to control robot using keyboard input
def control_robot_with_keyboard():
    while True:
        if keyboard.is_pressed('w'):
            move_forward()
        elif keyboard.is_pressed('s'):
            move_backward()
        elif keyboard.is_pressed('d'):
            turn_left()
        elif keyboard.is_pressed('a'):
            turn_right()
        elif keyboard.is_pressed('u'):
            turn_on_laser()
        elif keyboard.is_pressed('p'):
            turn_off_laser()
        elif keyboard.is_pressed('space'):
            stop()
        time.sleep(0.1)  # Delay to prevent CPU overload

# Create the main window
window = tk.Tk()
window.title("Robot Controller")

# Create buttons
forward_button = tk.Button(window, text="Move Forward", command=move_forward, width=15, height=2)
backward_button = tk.Button(window, text="Move Backward", command=move_backward, width=15, height=2)
left_button = tk.Button(window, text="Turn Left", command=turn_left, width=15, height=2)
right_button = tk.Button(window, text="Turn Right", command=turn_right, width=15, height=2)
stop_button = tk.Button(window, text="Stop", command=stop, width=15, height=2)
laser_on_button = tk.Button(window, text="Laser On", command=turn_on_laser, width=15, height=2)
laser_off_button = tk.Button(window, text="Laser Off", command=turn_off_laser, width=15, height=2)

# Status display
status_label = tk.Label(window, text="Status: ", font=('Arial', 14))

# Arrange buttons on grid
forward_button.grid(row=0, column=1, padx=5, pady=5)
backward_button.grid(row=2, column=1, padx=5, pady=5)
left_button.grid(row=1, column=0, padx=5, pady=5)
right_button.grid(row=1, column=2, padx=5, pady=5)
stop_button.grid(row=1, column=1, padx=5, pady=5)
laser_on_button.grid(row=3, column=0, padx=5, pady=5)
laser_off_button.grid(row=3, column=2, padx=5, pady=5)

# Status label positioning
status_label.grid(row=4, column=0, columnspan=3, pady=10)

# Start a thread to control the robot using keyboard input
keyboard_thread = threading.Thread(target=control_robot_with_keyboard, daemon=True)
keyboard_thread.start()

# Run the application
window.mainloop()
