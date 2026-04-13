# 11. 10번 연습문제에서 다음을 추가하여 프로그램을 작성하시오.
#     1) 트랙바를 추가해서 선의 굵기를 1~10픽셀로 조절한다.
#     2) 트랙바를 추가해서 원의 반지름을 1~50픽셀로 조절한다.

import numpy as np
import cv2

radius = 20
thickness = 1

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        print("1) 마우스 오른쪽 버튼 클릭 시 원(클릭 좌표에서 반지름 20화소)을 그린다.")
        cv2.circle(image, (x, y), radius, (0, 0, 0))
        cv2.imshow(title, image)
    elif event == cv2.EVENT_LBUTTONDOWN:
        print("2) 마우스 왼쪽 버튼 클릭 시 사각형(크기 30x30)을 그린다.")
        cv2.rectangle(image, (x, y, 30, 30), (0, 0, 0), thickness)
        cv2.imshow(title, image)

def onChangeThickness(value):
    global thickness

    thickness = value
    print("Thickness:", thickness)

def onChangeRadius(value):
    global radius

    radius = value
    print("Radius:", radius)

image = np.zeros((400, 600, 3), np.uint8)
image[:] = 255
title = "11 practice"

cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)

cv2.createTrackbar("Thickness", title, 1, 10, onChangeThickness)
cv2.createTrackbar("Radius", title, 20, 50, onChangeRadius)
cv2.waitKey(0)
cv2.destroyAllWindows()