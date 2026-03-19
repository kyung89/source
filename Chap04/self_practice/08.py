# 8. 200행, 300열의 행렬 2개를 만들어서 다음과 같이 배치하시오.

import numpy as np, cv2

image1 = np.zeros((200, 300, 3), np.uint8)
image2 = np.zeros((200, 300, 3), np.uint8)

cv2.namedWindow("win mode1")
cv2.namedWindow("win mode2")
cv2.imshow("win mode1", image1)
cv2.imshow("win mode2", image2)
cv2.moveWindow("win mode1", 0, 0)
cv2.moveWindow("win mode2", 300, 200)

cv2.waitKey(0)
cv2.destroyAllWindows()