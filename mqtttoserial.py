# -*- coding: iso-8859-1 -*-

import sys
import time
import serial
import threading
import paho.mqtt.subscribe as subscribe

DEVICE='/dev/ttyUSB0'
SPEED=9600 


def open_serial(dev, speed, show_info=False):
    ser = serial.Serial(dev, speed, timeout=1)
    time.sleep(0.5)
    if show_info:
        print ('\nStatus: %s ' % (ser.isOpen()))
        print ('Device: %s ' % (ser.name))
        print ('Settings:\n %s ' % (ser))
    return ser


def read_serial(ser, stop):
    while True:
        rec = ser.readline()
        if rec != b'':
            print (rec.decode('utf-8'))
        if stop():
            break
        # time.sleep(0.1)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        DEVICE = sys.argv[1]
    elif  len(sys.argv) == 3:
        DEVICE = sys.argv[1]
        SPEED = sys.argv[2]

    ser = open_serial(DEVICE, SPEED, True)

    stop=False

    threading.Thread(target=read_serial, args =(ser, lambda : stop, )).start()

    while True:
        m = subscribe.simple("#", hostname="localhost")
        x = (m.payload)
        ser.write(x)
# ######



