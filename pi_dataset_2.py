from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2
import Wisun_SEND
import threading
from threading import Thread

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 24
rawCapture = PiRGBArray(camera, size=(640, 480))
face_cascade = cv2.CascadeClassifier('/home/pi/Project_2/haarcascade_frontalface_default.xml')

image_path = "anh/anh.jpg"
tSend = threading.Thread(target = Wisun_SEND.Wisun_SEND,args = (image_path,))
tSend.start()
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors = 5, minSize = (100, 100), flags = cv2.CASCADE_SCALE_IMAGE)   
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        if len(faces):
       	    cv2.imwrite(image_path,roi_gray)
        cv2.imshow("Frame", image)
        if cv2.waitKey(1) & 0xff == ord("q"):
            exit()
        rawCapture.truncate(0)

