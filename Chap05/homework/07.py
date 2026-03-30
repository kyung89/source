# 다음의 컬러 영상파일(logo.jpg)을 입력 받아서 RGB의 3개 채널을 분리하고, 각 채널을 컬러 영상을 윈도우에 표시해보자.
# 즉 Red 채널은 빨간색으로, Green 채널은 초록색으로, Blue 채널은 파란색으로 표현되도록 다음의 프로그램을 완성하시오.

import numpy as np, cv2

logo = cv2.imread("images/logo.jpg", cv2.IMREAD_COLOR)
if logo is None: raise Exception("영상파일 읽기 오류")

blue, green, red = cv2.split(logo)

image = np.zeros(logo.shape[:2], dtype="uint8")
blue_img = cv2.merge((blue, image, image))
green_img = cv2.merge((image, green, image))
red_img = cv2.merge((image, image, red))

cv2.imshow("logo", logo)
cv2.imshow("blue_img", blue_img)
cv2.imshow("green_img", green_img)
cv2.imshow("red_img", red_img)
cv2.waitKey(0)
