import cv2 
import numpy as np 
import matplotlib.pyplot as plt    

img=cv2.imread("C://Users//jaswa//OneDrive//Desktop//shapes.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blured=cv2.GaussianBlur(gray,(5,5),0)

thresh=cv2.adaptiveThreshold(blured,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,15,4)

contors,hierachy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img,contors,-1,(255,0,0),2)

image_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')
plt.show()