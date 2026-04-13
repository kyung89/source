# 10. 다음의 마우스 이벤트 제어 프로그램을 작성하시오.
#     1) 마우스 오른쪽 버튼 클릭 시 원(클릭 좌표에서 반지름 20화소)을 그린다.
#     2) 마우스 왼족 버튼 클릭 시 사각형(크기 30x30)을 그린다

import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        print("1) 마우스 오른쪽 버튼 클릭 시 원(클릭 좌표에서 반지름 20화소)을 그린다.")
        cv2.circle(image, (x, y), 20, (0, 0, 0))
        cv2.imshow(title, image)
    elif event == cv2.EVENT_LBUTTONDOWN:
        print("2) 마우스 왼쪽 버튼 클릭 시 사각형(크기 30x30)을 그린다.")
        cv2.rectangle(image, (x, y, 30, 30), (0, 0, 0))
        cv2.imshow(title, image)

image = np.zeros((400, 400, 3), np.uint8)
image[:] = 255
title = "10 practice"

cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()