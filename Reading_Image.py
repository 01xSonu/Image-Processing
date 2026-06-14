import cv2
import numpy as np

#reading an image
img=cv2.imread("image/car.png")

print(type(img ))
print(img.shape)
print(img)

#Display Image
cv2.imshow("Picture",img)
cv2.waitKey(0)


