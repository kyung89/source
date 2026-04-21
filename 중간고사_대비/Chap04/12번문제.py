# 12. 예제_4.2.3dls 05.event_trackbar.py 에서 화살표 키로 트랙바를 이동하는 코드를 추가하시오.

import numpy as np
import cv2

def onChange(value):
    global image, title

    add_value = value - int(image[0][0])
    print("추가 화소값:", add_value)
    # image[:] = image + add_value
    if  add_value > 0 : image = image + add_value            		# 행렬과 스칼라 덧셈 수행
    else: image = image - abs(add_value)  # 행렬과 스칼라 덧셈 수행
    cv2.imshow(title, image)

image = np.zeros((300, 500), dtype=np.uint8)

title = "Trackbar Event"
cv2.imshow(title, image)
cv2.createTrackbar('Brightness', title, image[0][0], 255, onChange)

while True:
    key = cv2.waitKeyEx(100)
    if key == 27: break

    value = cv2.getTrackbarPos('Brightness', title)

    if key in (2424832, 2621440): # 감소
        value = max(0, value - 10)
        cv2.setTrackbarPos('Brightness', title, value)
    elif key in (2490368, 2555904): # 증가
        value = min(255, value + 10)
        cv2.setTrackbarPos('Brightness', title, value)
    cv2.imshow(title, image)

cv2.waitKey(0)
cv2.destroyAllWindows()