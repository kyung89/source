# 6. 300행, 400열의 행렬을 회색 바탕색(100)으로 생성해서 500행, 600열의 윈도우에 표시하시오.
import numpy as np
import cv2

print()
print("6. 300행, 400열의 행렬을 회색 바탕색(100)으로 생성해서 500행, 600열의 윈도우에 표시하시오.")
print()

image = np.zeros((300, 400), np.uint8)
image[:] = 100
title = "06 practice"

cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
cv2.imshow(title, image)
cv2.resizeWindow(title, 600, 500) # winname, width, height
cv2.waitKey(0)
cv2.destroyAllWindows()

