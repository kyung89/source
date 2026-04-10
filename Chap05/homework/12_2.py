import cv2
import numpy as np

image = cv2.imread("images/color.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상을 읽을 수 없습니다.")

result = image.copy()

# 관심영역 1: 밝기 증가
roi1 = result[60:160, 20:120]
roi1 = cv2.add(roi1, 50)
result[60:160, 20:120] = roi1

# 관심영역 2: 화소 대비 증가
roi2 = result[160:260, 120:220]
roi2 = cv2.convertScaleAbs(roi2, alpha=1.8, beta=0)
result[160:260, 120:220] = roi2

# 관심영역 표시
cv2.rectangle(result, (20, 60), (120, 160), (0, 255, 0), 2)
cv2.rectangle(result, (120, 160), (220, 260), (255, 0, 0), 2)

cv2.imshow("original", image)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()