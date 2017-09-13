import time
import serial
import sys


def arduino_1(message):
    tmp_msg = "/dev/cu.usbmodem1411"
    ser = serial.Serial(tmp_msg)
    ser.baudrate = 9600
    ser.timeout = 1
    msg = bytes(message, 'utf-8')
    ser.write(msg)
    time.sleep(0.1)
    return "OK"
