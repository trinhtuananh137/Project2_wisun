import cv2
import numpy as np
import Wisun_SEND
import threading
from threading import Thread
import os
import sys
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
image_path = "./anh/anh.jpg"
tSend = threading.Thread(target = Wisun_SEND.Wisun_SEND,args = (image_path,))
tSend.start()
while cv2.waitKey(30)&0xFF != ord('q'):
    ret,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        cv2.imshow('img',img)
        cv2.imwrite(image_path, img[y:y+h,x:x+w])
    cv2.imshow('img',img)

cv2.destroyAllWindows()
#cap.release()
os.remove(image_path)
sys.exit()



