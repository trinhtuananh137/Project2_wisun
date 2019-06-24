import picamera
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import Wisun_SEND
#import os
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 24
rawCapture = PiRGBArray(camera, size=(640, 480))
#Load a cascade file for detecting faces
face_cascade = cv2.CascadeClassifier('/home/pi/Project_2/haarcascade_frontalface_default.xml')
#image_path = "anh/anh.jpg"
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # convert frame to array
    image = frame.array
    #Convert to grayscale
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #Look for faces in the image using the loaded cascade file
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors = 5, minSize = (100, 100), flags = cv2.CASCADE_SCALE_IMAGE)

    #Draw a rectangle around every found face
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        #cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        print(x,y,w,h)
	dim = (80,80)
	resized = cv2.resize(roi_gray, dim, interpolation = cv2.INTER_AREA)
    #Save the result image
    if len(faces):
        item_path = "anh/anh.jpg"
        cv2.imwrite(item_path,resized)
	Wisun_SEND.Wisun_SEND(item_path)
#	os.remove("anh/anh.jpg")
    # display a frame    
    #cv2.imshow("Frame", image)
    #wait for 'q' key was pressed and break from the loop
    #if cv2.waitKey(1) & 0xff == ord("q"):
	    #exit()
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)