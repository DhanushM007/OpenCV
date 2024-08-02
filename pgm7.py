#4 quad pgm


import numpy as np  
import cv2 
import matplotlib.pyplot as plt   

img=cv2.imread("C://Users//jaswa//OneDrive//Desktop//rnsit.jpg")

h,w=img.shape[:2]

quad1=img[:h//2,:w//2]
quad2=img[:h//2,w//2:]
quad3=img[h//2:,:w//2]
quad4=img[h//2:,w//2:]

plt.figure(figsize=(10,5))
plt.subplot(2,2,1)
plt.imshow(cv2.cvtColor(quad1,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("1")

plt.subplot(2,2,2)
plt.imshow(cv2.cvtColor(quad2,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("2")

plt.subplot(2,2,3)
plt.imshow(cv2.cvtColor(quad3,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("3")

plt.subplot(2,2,4)
plt.imshow(cv2.cvtColor(quad4,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("4")

plt.show()