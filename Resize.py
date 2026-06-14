import cv2
import numpy as np
img=cv2.imread("Image/car.png")

img_resize=cv2.resize(img,(600,300))
#Exactly half dimension
#if(x,y) x-> Width, y-> height
img_half_dimesnsion=cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))

print(img_resize.shape)
print(img_resize)

cv2.imshow("Picture",img_resize)
cv2.waitKey(0)