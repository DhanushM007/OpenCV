#blur and smooth

import cv2 
import numpy as np 
import matplotlib.pyplot as plt    

img=cv2.imread("C://Users//jaswa//OneDrive//Desktop//rnsit.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur=cv2.GaussianBlur(gray,(5,5),0)

smooth=cv2.bilateralFilter(gray,9,75,75)


plt.figure(figsize=(10,5))
plt.subplot(1,3,1)
plt.imshow(gray,cmap='gray')
plt.title("original")
plt.axis('off')


plt.subplot(1,3,2)
plt.imshow(blur,cmap='gray')
plt.title("blurred")
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(smooth,cmap='gray')
plt.title("smooth")
plt.axis('off')

plt.show()



