#rotate,scale and translate

import numpy as np    
import cv2 
import matplotlib.pyplot as plt      

def translate_image(image,dx,dy):
    h,w=image.shape[:2]
    translate_mat=np.float32([[1,0,dx],[0,1,dy]])
    translated_image=cv2.warpAffine(image,translate_mat,(w,h))
    return translated_image  

img=cv2.imread("C://Users//jaswa//OneDrive//Desktop//rnsit.jpg")

image_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
height,width=img.shape[:2]
center=(width//2,height//2)

rot_val=int(input("enter the rot value:"))
while rot_val<-180 or rot_val>180:
    rot_val=int(input("Invalid. enter again:"))
    
sca_val=int(input("enter the scale value:"))
while sca_val<0.1 or sca_val>10:
    rot_val=int(input("Invalid. enter again:"))
    
h=int(input("enter h value:"))
v=int(input("enter v value:"))

rot_mat=cv2.getRotationMatrix2D(center=center,angle=rot_val,scale=1)
rotated_image=cv2.warpAffine(src=img,M=rot_mat,dsize=(width,height))

sca_mat=cv2.getRotationMatrix2D(center=center,angle=0,scale=sca_val)
scaled_image=cv2.warpAffine(src=rotated_image,M=sca_mat,dsize=(width,height))

translated_image=translate_image(scaled_image,h,v)

plt.figure(figsize
           =(10,5))
plt.subplot(2,2,1)
plt.title("original image")
plt.imshow(image_rgb)
plt.axis("off")

plt.subplot(2,2,2)
plt.title("rotated image")
plt.imshow(cv2.cvtColor(rotated_image,cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(2,2,3)
plt.title("scaled image")
plt.imshow(cv2.cvtColor(scaled_image,cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(2,2,4)
plt.title("final transformed image")
plt.imshow(cv2.cvtColor(translated_image,cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.show()

        
