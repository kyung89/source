# 09. 600행, 400열의 윈도우를 만들고, 영상 안의 (100, 100) 좌표에 200 x 300 크기의 빨간색 사각형을 그리시오.

import numpy as np, cv2

image = np.full((600, 400, 3), (255, 255, 255), np.uint8)
cv2.rectangle(image, (100, 100), (300, 400), (0, 0, 255), cv2.FILLED)
cv2.imshow("image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()