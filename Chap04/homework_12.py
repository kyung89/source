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
    if key == 27: break

    try:
        result = switch_case[key]
        print(result)
        if key == 2424832: # 왼쪽 화살표키 입력
            if image[0][0] == 0: value = image[0][0]
            else: value = image[0][0] - 10
            cv2.setTrackbarPos(bar_name, title, value)
        elif key == 2490368: # 윗쪽 화살표키 입력
            if image[0][0] == 255: value = image[0][0]
            else: value = image[0][0] + 10
            cv2.setTrackbarPos(bar_name, title, value)
        elif key == 2555904: # 오른쪽 화살표키 입력
            if image[0][0] == 255: value = image[0][0]
            else: value = image[0][0] + 10
            cv2.setTrackbarPos(bar_name, title, value)
        elif key == 2621440: # 아래쪽 화살표키 입력
            if image[0][0] == 0: value = image[0][0]
            else: value = image[0][0] - 10
            cv2.setTrackbarPos(bar_name, title, value)
    except KeyError:
        result = -1

cv2.destroyAllWindows()