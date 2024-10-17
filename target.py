import keyboard
import serial
import time

ser = serial.Serial('COM8', 9600)

def move_forward():
    ser.write(b'w')

def move_backward():
    ser.write(b's')

def turn_left():
    ser.write(b'd')

def turn_right():
    ser.write(b'a')

def stop():
    ser.write(b'm')

def turn_on_laser():
    ser.write(b'u')

def turn_off_laser():
    ser.write(b'p')


def control_robot():
    print(" f,b,l,r for movement, and u,p for laser ")
    print("Press Space to stop, and U to turn on laser, P to turn it off.")
    while True:
        if keyboard.is_pressed('w'):
            print("f")
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

        time.sleep(0.1)

control_robot()