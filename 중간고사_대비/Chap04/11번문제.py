# 11. 10번 연습문제에서 다음을 추가하여 프로그램을 작성하시오.
# 1) 트랙바를 추가해서 선의 굵기를 1~10픽셀로 조절한다.
# 2) 트랙바를 추가해서 원의 반지름을 1~50픽셀로 조절한다.

import numpy as np, cv2

thickness = 1
radius = 20

def onMouse(event, x, y, flags, param):
    global image

    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, (x, y), radius, (0, 0, 0), thickness)
    elif event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(image, (x, y), (x + 30, y + 30), (0, 0, 0), thickness)
    cv2.imshow("image", image)

def setThickness(value):
    global thickness
    if value == 0: thickness = 1
    else: thickness = value

def setRadius(value):
    global radius
    if value == 0: radius = 1
    else: radius = value

image = np.full((300, 300, 3), (255, 255, 255), np.uint8)
cv2.imshow("image", image)

cv2.setMouseCallback("image", onMouse)
cv2.createTrackbar("Thickness", "image", thickness, 10, setThickness)
cv2.createTrackbar("Radius", "image", radius, 50, setRadius)

cv2.waitKey(0)
cv2.destroyAllWindows()