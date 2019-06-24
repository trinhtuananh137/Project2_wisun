import serial
from serial import Serial
from time import sleep

PANID = '1234'
CH = '21'
PWD = '0123456789AB'
RBID = '00112233445566778899AABBCCDDEEFF'
CORDIP = 'FE80:0000:0000:0000:021D:1290:0004:631F'

ser = serial.Serial(    
    port='/dev/ttyUSB0',
    baudrate=115200,
    timeout = 10,
    parity = serial.PARITY_NONE,
    bytesize=serial.EIGHTBITS,
    rtscts = True,
    dsrdtr = False
)
#RESET wisun
_mes = ""
cmd = "SKRESET\r\n"
mes = b""
ser.write(cmd.encode('ascii'))
mes = ser.readline()
while mes != b'':
    _mes = _mes + mes.decode('ascii')
    mes = ser.readline()
if ("OK" in _mes): 
    print(_mes)
    _mes = ""
    print("reset xong")
    cmd = "SKSREG SFE 0\r\n"
    ser.write(cmd.encode('ascii'))
    mes = ser.readline()
    while mes != b'':
        _mes = _mes + mes.decode('ascii')
        mes = ser.readline()
if ("OK" in _mes): 
    print(mes.decode('ascii'))
    print("Da tat echo")
    cmd = "SKSETPWD C "+PWD +"\r\n"
    ser.write(cmd.encode('ascii'))
    mes = ser.readline()
if ("OK" in mes.decode('ascii')): 
    print(mes.decode('ascii'))
    print("set pwd xong")
    cmd = "SKSETRBID "+RBID+"\r\n"
    ser.write(cmd.encode('ascii'))
    mes = ser.readline()
else:
    print("setpwd khong thanh cong")     
if ("OK" in _mes): 
    print(_mes)
    print("set rbid xong")
    cmd = "SKSREG S2 " + CH + "\r\n"
    ser.write(cmd.encode('ascii'))
    mes = ser.readline()
else:
    print("set rbid khong thanh cong")
if ("OK" in mes.decode('ascii')): 
    print(mes.decode("ascii"))
    cmd = "SKSREG S3 "+PANID + "\r\n"
    ser.write(cmd.encode('ascii'))
    mes = ser.readline()
else:
    print("set panid khong thanh cong")
if ("OK" in mes.decode('ascii')): 
    print(mes.decode("ascii"))
    cmd = "SKJOIN "+ CORDIP + "\r\n"
    ser.write(cmd.encode('ascii'))
    mes = ser.readline()
    _mes = b""
    while not(b'EVENT 25' in mes):
        _mes = _mes + mes
        mes = ser.readline()
    _mes = mes
if (b"EVENT 25" in _mes): 
    print ("Join thanh cong")
    while 1:
        cmd = "SKSENDTO 1 "+CORDIP+" 0E1A 1 0007 SANSLAB" + "\r\n"
        ser.write(cmd.encode('ascii'))
        mes = ser.readline()
        while mes != b'':
            print(mes.decode("ascii"),end = '')
            mes = ser.readline()
else:
    print("ket noi that bai, kiem tra lai")