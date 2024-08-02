import cv2 
import numpy as np 
import matplotlib.pyplot as plt    

img=cv2.imread("C://Users//jaswa//OneDrive//Desktop//face.jpeg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

detect_face=face_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)

for(x,y,w,h) in detect_face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
plt.title("faces")
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

