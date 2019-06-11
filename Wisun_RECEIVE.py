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

while 1:
    mes_receive = ser_receive.readline()
    if not(b"begin" in mes_receive):
        continue
    else:
        mes_receive = ser_receive.readline()
    if os.path.isfile("imageToSave.png"):
        os.remove("imageToSave.png")
    fh = open("imageToSave.png","ab")
    while not(b'end' in mes_receive):    
        if mes_receive != b'':
            a = mes_receive[121:]
            #b = a[121:]
            #c = b.encode()
            try:
                fh.write(base64.b64decode(a))
            except:
                break
        mes_receive = ser_receive.readline()
    #mes_receive = ser_receive.readline()
    fh.close()
    if os.path.isfile("imageToSave.png"):    
        fh = open("imageToSave.png", "rb")
        bfh = fh.read()
        if bfh != b"":
            fh_proc = open("imageToProcess.png","wb")
            fh_proc.write(bfh)
            fh_proc.close()
        fh.close()    
    mes_receive = ser_receive.readline()
    #os.remove("imageToSave.png")

        
    
