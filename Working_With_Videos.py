import cv2
import numpy as np
cam=cv2.VideoCapture(0) #Open local Webcam

while True:
    ret,frame=cam.read()
    cv2.imshow("Webcam",frame)


    if cv2.waitKey(1) & 0xFF==ord('x'):
        break
cam.release()     #release webcam
cv2.destroyAllWindows()