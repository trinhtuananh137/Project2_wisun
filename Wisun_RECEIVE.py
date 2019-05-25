import serial
from serial import Serial
#from time import sleep
#import time
#import re
import os
import base64

ser_receive = serial.Serial(    
    port='COM4',
    baudrate=115200,
    timeout = 5,
    parity = serial.PARITY_NONE,
    bytesize=serial.EIGHTBITS,
    rtscts = True,
    dsrdtr = False
)
receive = ''
mes_receive = ser_receive.readline()
if os.path.isfile("imageToSave.png"):
        os.remove("imageToSave.png")
while not(b'end' in mes_receive):    
    fh = open("imageToSave.png", "ab")
    if mes_receive != b'':
        a = mes_receive.decode()
        b = a[121:]
        c = b.encode()
        fh.write(base64.b64decode(c))
    mes_receive = ser_receive.readline()
fh.close()
        
    
