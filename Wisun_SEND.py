import serial
import base64
import cv2
import numpy as np
from PIL import Image
from serial import Serial
from time import sleep

CORDIP = 'FE80:0000:0000:0000:021D:1290:0004:631F'

def d2h(x):
    str = hex(x)
    _str = str[2:len(str)]
    _len = len(_str)
    if(_len ==1):
        _str = "000" + _str
    elif(_len ==2):
        _str = "00" + _str
    elif(_len ==3):
        _str = "0" + str
    return(_str)
image_path = "./face.jpg"
imageFile = open(image_path, "rb")
bstr = base64.b64encode(imageFile.read())
_str = bstr.decode()
imageFile.close()
_len  = len(_str)
m = int(_len/200) * 200
send = []
for i in range(0,m + 1,200):
    send.append(_str[0 + i:200 +i])

ser_send = serial.Serial(    
    port='COM5',
    baudrate=115200,
    timeout = 10,
    parity = serial.PARITY_NONE,
    bytesize=serial.EIGHTBITS,
    rtscts = True,
    dsrdtr = False
)

# cmd = "SKSENDTO 1 "+ CORDIP +" 0E1A 1 0005 begin\r\n"
# ser_send.write(cmd.encode('ascii'))

for s in send:
    l = ''
    l = l + d2h(len(s))
    cmd = "SKSENDTO 1 "+ CORDIP +" 0E1A 1 " + l + " " + s + '\r\n'
    ser_send.write(cmd.encode('ascii')) 
    mes_send = ser_send.readline()    
    while not(b'OK' in mes_send):
        mes_send = ser_send.readline()
cmd = "SKSENDTO 1 "+ CORDIP +" 0E1A 1 0003 end\r\n"
ser_send.write(cmd.encode('ascii'))
mes_send = ser_send.readline()    
while not(b'OK' in mes_send):
    mes_send = ser_send.readline()
