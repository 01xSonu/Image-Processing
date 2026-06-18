import cv2
cap=cv2.VideoCapture(0)

while True:

    ret , frame=cap.read()

    #RGB to Gray
    gray_vid=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("webcam",gray_vid)



    if cv2.waitKey(1) & 0xFF==ord('x'):
        break
cap.release()
cv2.destroyAllWindows()