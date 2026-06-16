import cv2
import numpy as np

#reading an image
img=cv2.imread("image/car.png")

#Convert to GrayScale
img_grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

print(type(img_grey))
print(img_grey.shape)
print(img_grey)

#Display Image
cv2.imshow("Picture",img_grey)
cv2.waitKey(0)