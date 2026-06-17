import cv2

start_x, start_y = -1, -1


def draw(event, x, y, flags, param):
    global start_x, start_y, img

    if event == cv2.EVENT_LBUTTONDOWN:  #Left button down (Start Drawing)

        start_x, start_y = x, y

    elif event == cv2.EVENT_LBUTTONUP:  #LEft button up (End Drawing)

        cv2.rectangle(img,
                      (start_x, start_y),
                      (x, y),
                      (255, 0, 0),
                      3)

img = cv2.imread("Image/people.png")

cv2.namedWindow("Picture")
cv2.setMouseCallback("Picture", draw)

while True:
    cv2.imshow("Picture", img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()