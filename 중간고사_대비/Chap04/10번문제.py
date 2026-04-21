# 10. 다음의 마우스 이벤트 제어 프로그램을 작성하시오.
# 1) 마우스 오른쪽 버튼 클릭 시 원(클릭좌표에서 반지름 20화소)을 그린다.
# 2) 마우스 왼쪽 버튼 클릭 시 사각형(크기 30 x 30)을 그린다.

import numpy as np, cv2

def onMouse(event, x, y, flags, param):
    global image

    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, (x, y), 20, (0, 0, 0), 1)
    elif event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(image, (x, y), (x + 30, y + 30), (0, 0, 0), 1)
    cv2.imshow("image", image)

image = np.full((300, 300, 3), (255, 255, 255), np.uint8)
cv2.imshow("image", image)

cv2.setMouseCallback("image", onMouse)

cv2.waitKey(0)
cv2.destroyAllWindows()