# 06. 300행, 400열의 행렬을 회색 바탕색으로(100) 생성해서 500행, 600열의 윈도우에 표시하시오.

import numpy as np, cv2

image = np.zeros((300, 400), np.uint8)
image[:] = 100

cv2.imshow("06", image)
cv2.resizeWindow("06", 600, 500)

cv2.waitKey(0)
cv2.destroyAllWindows()