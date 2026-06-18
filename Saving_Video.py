import cv2
cap=cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'MJPG') #four char code
out=cv2.VideoWriter('output_Video.avi',fourcc, 20.0, (640,480))

while True:

    ret , frame=cap.read()
    out.write(frame)
    #RGB to Gray
    gray_vid=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("webcam",gray_vid)



    if cv2.waitKey(1) & 0xFF==ord('x'):
        break
cap.release()
cv2.destroyAllWindows()

