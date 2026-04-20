# 12. 예제_4.2.3인 05.event_trackbar.py에서 화살표 키로 트랙바를 이동하는 코드를 추가하시오.

import numpy as np
import cv2

def onChange(value):
    global image, title

    add_value = value - int(image[0][0])
    print("추가 화소값:", add_value)
    #image[:] = image + add_value
    if  add_value > 0 : image = image + add_value            		# 행렬과 스칼라 덧셈 수행
    else: image = image - abs(add_value)  # 행렬과 스칼라 덧셈 수행
    cv2.imshow(title, image)

switch_case = {
    2424832: "왼쪽 화살표키 입력",
    2490368: "윗쪽 화살표키 입력",
    2555904: "오른쪽 화살표키 입력",
    2621440: "아래쪽 화살표키 입력"
}

image = np.zeros((300, 500), dtype=np.uint8)

title = "Trackbar Event"
cv2.imshow(title, image)

bar_name = "Brightness"
cv2.createTrackbar(bar_name, title, image[0][0], 255, onChange)

while True:
    key = cv2.waitKeyEx(100)
    if key == 27:
        break

    if key in switch_case:
        print(switch_case[key])

        value = cv2.getTrackbarPos(bar_name, title)

        if key in (2424832, 2621440):   # 왼쪽, 아래쪽
            value = max(0, value - 10)
        elif key in (2490368, 2555904): # 위쪽, 오른쪽
            value = min(255, value + 10)

        cv2.setTrackbarPos(bar_name, title, value)

cv2.destroyAllWindows()