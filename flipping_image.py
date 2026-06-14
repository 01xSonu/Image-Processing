import cv2
import numpy as np

img=cv2.imread("image/dolphin.png")

#flip the image
#0 for Vertical flip
#1 for Horizontal flip
img_flip=cv2.flip(img,1)

print(img_flip.shape)
print(img_flip)
cv2.imshow("IMage",img_flip)
cv2.waitKey(0)
