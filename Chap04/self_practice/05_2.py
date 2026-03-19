# 5. 다음 예시 코드의 실행 결과를 설명하시오.

import numpy as np, cv2

image = np.zeros((400, 600, 3), np.uint8)
image[:] = (255, 255, 255)
pt1, pt2 = (50, 100), (200, 300)

cv2.line(image, pt1, pt2, (0, 255, 0), 2)
cv2.rectangle(image, pt2, (300, 400), (0, 0, 255), -1, cv2.LINE_4, 1)

cv2.imshow('Line & Rectangle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()