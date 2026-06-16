import cv2
import numpy as np
#creating an image (black)
img=np.zeros((512,512,3))

#creating an image(white)
#img=np.ones((512,512,3))

#Rectangle Shape
cv2.rectangle(img,(10,10),(400,400),(255,0,0),3) # if thickness=NEG val. then it fill the Shape completely instead of drawing only its border.
#Circle
cv2.circle(img,(200,400),50,(0,100,0),1)
#Line
cv2.line(img,(100,300),(200,400),(0,0,255),2)
#Text
cv2.putText(img,org=(250,400),fontScale=2,color=(255,0,0),thickness=2,lineType=cv2.LINE_AA,text="Image",fontFace=cv2.FONT_HERSHEY_PLAIN)
cv2.imshow("Image",img)
cv2.waitKey(0)