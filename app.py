import time
import serial
import sys

from flask import Flask


app = Flask(__name__)

@app.route("/on")
def arduino_1():
	msg=bytes("o",'utf-8')
	ser.write(msg)
	time.sleep(0.1)
	return "LED 1 ON!"

@app.route("/off")
def arduino_2():
	msg=bytes("p",'utf-8')
	ser.write(msg)
	time.sleep(0.1)
	return "LED 2 ON!"


if __name__ == "__main__":
	tmp_msg = "/dev/cu.usbmodem1411"
	ser = serial.Serial(tmp_msg)
	ser.baudrate = 9600
	ser.timeout = 1
	print(ser.portstr)

	app.run("127.0.0.1",1234)
	ser.close()
