# 영상파일을 읽어서 메인 윈도우에 다음과 같이 출력하시오.
# 1) 메인 윈도우의 특정 부분 2곳을 관심영역으로 지정한다.
# 2) 관심영역1는 영상의 밝기를 50만큼 밝게 한다.
# 3) 관심영역2은 영상의 화소대비를 증가시킨다.

import numpy as np, cv2

image = cv2.imread("images/color.jpg", cv2.IMREAD_COLOR)

mask1 = np.zeros(image.shape[:2], dtype="uint8")
mask1[60:160, 20:120] = 255

mask2 = np.zeros(image.shape[:2], dtype="uint8")
mask2[160:260, 120:220] = 255

mask3 = cv2.bitwise_or(mask1, mask2)
mask3 = cv2.bitwise_not(mask3)

background = cv2.bitwise_and(image, image, mask=mask3)
dst1 = cv2.bitwise_and(image, image, mask=mask1)
dst2 = cv2.bitwise_and(image, image, mask=mask2)

dst1[60:160, 20:120] = cv2.add(dst1[60:160, 20:120], 50)
dst2 = cv2.convertScaleAbs(dst2, alpha=2.0, beta=0)

result = cv2.bitwise_xor(background, dst1)
result = cv2.bitwise_xor(result, dst2)

# cv2.imshow('background', background)
# cv2.imshow('dst1', dst1)
# cv2.imshow('dst2', dst2)
cv2.imshow('result', result)
cv2.waitKey()