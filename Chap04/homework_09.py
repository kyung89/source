# 9. 600행, 400열의 윈도우를 만들고, 영상 안의 (100, 100) 좌표에 200x300 크기의 빨간 색 사각형을 그리시오.
import numpy as np
import cv2

print()
print("9. 600행, 400열의 윈도우를 만들고, 영상 안의 (100, 100) 좌표에 200x300 크기의 빨간 색 사각형을 그리시오.")
print()

red = (0, 0, 255)
image = np.zeros((600, 400, 3), np.uint8)
image[:] = 255
title = "09 practice"

cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
cv2.rectangle(image, (100, 100, 300, 200), red, cv2.FILLED)

cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()

