# 08. 200행, 300열의 행렬을 만들어서 다음과 같이 배치하시오.

import numpy as np, cv2

image1 = np.full((200, 300, 3), (0, 0, 0), np.uint8)
image2 = np.full((200, 300, 3), (0, 0, 0), np.uint8)

cv2.imshow("image1", image1)
cv2.imshow("image2", image2)

cv2.moveWindow("image1", 0, 0)
cv2.moveWindow("image2", 300, 200)

cv2.waitKey(0)
cv2.destroyAllWindows()