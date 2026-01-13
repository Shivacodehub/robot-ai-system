
import serial
import time
import os

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
time.sleep(2)

def send(cmd):
    ser.write((cmd + "\n").encode())
