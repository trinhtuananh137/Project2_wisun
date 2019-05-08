import base64
import cv2
import numpy as np
from PIL import Image
image_path = "./face.jpg"
encode_path = "./base64Encode.txt"
file = open(encode_path,"wb+")
imageFile = open(image_path, "rb")
str = base64.b64encode(imageFile.read())
file.write(str)
file.close()
imageFile.close()
fh = open("imageToSave.png", "wb")
fh.write(base64.b64decode(str))
fh.close()