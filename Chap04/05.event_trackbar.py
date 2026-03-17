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

image = np.zeros((300, 500), dtype=np.uint8)

title = "Trackbar Event"
cv2.imshow(title, image)

cv2.createTrackbar('Brightness', title, image[0][0], 255, onChange)
cv2.waitKey(0)
cv2.destroyAllWindows()