import cv2

def draw(event, x, y, flags, param):


    if event == cv2.EVENT_LBUTTONDOWN:  #Left button down (Start Drawing)
        cv2.circle(img,(x,y),radius=20,color=(0,0,255),thickness=3)



img = cv2.imread("Image/people.png")

cv2.namedWindow("Picture")
cv2.setMouseCallback("Picture", draw)

while True:
    cv2.imshow("Picture", img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()