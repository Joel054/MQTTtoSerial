# -*- coding: iso-8859-1 -*-

import sys
import time
import serial
import threading
import paho.mqtt.subscribe as subscribe
import paho.mqtt.publish as publish

# DEVICE='/dev/ttyUSB0'
DEVICE= '/dev/ttyACM1'
# SPEED=9600
SPEED=115200

HOSTNAME= "10.0.1.15"
# HOSTNAME= "localhost"

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
        print ("passei",rec)
        if len(rec) != 0:
            print ("passei 2")
        #print (rec.decode())
            publish.single("/teste/", rec.decode(), hostname = HOSTNAME)
        # if stop():
        #     break
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
        # m = subscribe.simple("#", hostname="localhost")
        # x = (m.payload)
        # ser.write(x)
        print("while true")
        time.sleep(3)
    
# ######
