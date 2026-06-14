import cv2
import numpy as np

#reading an image
img=cv2.imread("image/car.png")

#cropping
#Order is [row, column]=[y,x]
#y->Height , x->Width
# origin is top left .

img_crop=img[100:300,400:800]

print(img_crop)
cv2.imshow("Image",img_crop)
cv2.waitKey(0)

# for saving this picture
cv2.imwrite("Croped_Image.png",img_crop)


