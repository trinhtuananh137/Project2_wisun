import serial
from serial import Serial
from time import sleep
import time
import re

PANID = '1234'
CH = '21'
PWD = '0123456789AB'
RBID = '00112233445566778899AABBCCDDEEFF'

ser = serial.Serial(    
    port='COM4',
    baudrate=115200,
    timeout = 5,
    parity = serial.PARITY_NONE,
    bytesize=serial.EIGHTBITS,
    rtscts = True,
    dsrdtr = False
)

res = []
_res =""
#RESET wisun
cmd = "SKRESET"
ser.write(cmd.encode('ascii')+ bytes([13]))
mes = ser.read()
while mes != b'':
    try:
        _mes = mes.decode()
        res.append(_mes)
        #time.sleep(0.05)
        mes = ser.read()
    except serial.SerialTimeoutException:
        print("Could not received respond")
_res = "".join(res)
#SETPWD wisun
if re.findall("OK",_res):
    print("RESET thanh cong")
    res = []
    _res =""
    cmd = "SKSETPWD C " + PWD
    ser.write(cmd.encode('ascii')+ bytes([13]))
    mes = ser.read()
    while mes != b'':
        try:
            _mes = mes.decode()
            res.append(_mes)
            #time.sleep(0.05)
            mes = ser.read()
        except serial.SerialTimeoutException:
            print("Could not received respond")
    _res = "".join(res)
#SETRBID wisun
if re.findall("OK",_res):
    print("SETPWD thanh cong")
    res = []
    _res =""
    cmd = "SKSETRBID " + RBID
    ser.write(cmd.encode('ascii')+ bytes([13]))
    mes = ser.read()
    while mes != b'':
        try:
            _mes = mes.decode()
            res.append(_mes)
            #time.sleep(0.05)
            mes = ser.read()
        except serial.SerialTimeoutException:
            print("Could not received respond")
    _res = "".join(res)
#SCAN channel
if re.findall("OK",_res):
    print("SETRBID thanh cong")
    res = []
    _res =""
    cmd = "SKSCAN 0 FFFFFFFF 4"
    ser.write(cmd.encode('ascii')+ bytes([13]))
    mes = ser.read()
    while mes != b'':
        try:
            _mes = mes.decode()
            res.append(_mes)
            #time.sleep(0.05)
            mes = ser.read()
        except serial.SerialTimeoutException:
            print("Could not received respond")
    _res = "".join(res)
#SKSREG
if re.findall("EEDSCAN",_res):
    print("scan xong")
    res = []
    _res =""
    cmd = "SKSREG S2 " + CH 
    ser.write(cmd.encode('ascii')+ bytes([13]))
    mes = ser.read()
    while mes != b'':
        try:
            _mes = mes.decode()
            res.append(_mes)
            #time.sleep(0.05)
            mes = ser.read()
        except serial.SerialTimeoutException:
            print("Could not received respond")
    _res = "".join(res)
if re.findall("OK",_res):
    print("SKSREG S2 xong")
    res = []
    _res =""
    cmd = "SKSREG S3 " + PANID 
    ser.write(cmd.encode('ascii')+ bytes([13]))
    mes = ser.read()
    while mes != b'':
        try:
            _mes = mes.decode()
            res.append(_mes)
            #time.sleep(0.05)
            mes = ser.read()
        except serial.SerialTimeoutException:
            print("Could not received respond")
    _res = "".join(res)
if re.findall("OK",_res):
    print("SKSREG S3 xong")
    res = []
    _res =""
    cmd = "SKSREG S15 1" 
    ser.write(cmd.encode('ascii')+ bytes([13]))
    mes = ser.read()
    while mes != b'':
        try:
            _mes = mes.decode()
            res.append(_mes)
            #time.sleep(0.05)
            mes = ser.read()
        except serial.SerialTimeoutException:
            print("Could not received respond")
    _res = "".join(res)
if re.findall("OK",_res):
    print("SKSREG S15 xong")
    res = []
    _res =""
    cmd = "SKSTART" 
    ser.write(cmd.encode('ascii')+ bytes([13]))
    mes = ser.read()
    while mes != b'':
        try:
            _mes = mes.decode()
            res.append(_mes)
            #time.sleep(0.05)
            mes = ser.read()
        except serial.SerialTimeoutException:
            print("Could not received respond")
    _res = "".join(res)
if re.findall("OK",_res):
    print("Bat dau lam COORDINATOR") 