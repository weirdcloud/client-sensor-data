import serial
import requests
import json

from urls import *

# creating serial connection
port = '/dev/ttyACM1'
baud = 115200

ser = serial.Serial(port, baud, timeout=None)


while True:
    # get data from serial
    reading = ser.readline().decode()
    print("reading:", reading, end='')
    data = json.loads(reading)
    print("data:", data)

    # send data to server and get response
    res = requests.request("POST", url_home, json=data)
    print(res.status_code, res.text)
    print(res.json())
