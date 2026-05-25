# 코드를 완전히 외우고, 여러번 다시 풀것!

import numpy as np
import cv2

image = cv2.imread("flower.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상파일 읽기 에러")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

h_bins = 30
s_bins = 48

hist = cv2.calcHist(
    [hsv],
    [0, 1],
    None,
    [h_bins, s_bins],
    [0, 180, 0, 256]
)

hist_norm = cv2.normalize(hist, None, 0, 255, cv2.NORM_MINMAX)
hist_norm = hist_norm.astype(np.uint8)

# HSV 색상 히스토그램 영상 생성
hist_color_hsv = np.zeros((h_bins, s_bins, 3), np.uint8)

for h in range(h_bins):
    for s in range(s_bins):
        hue = int(h * 180 / h_bins)
        sat = int(s * 256 / s_bins)
        val = hist_norm[h, s]

        hist_color_hsv[h, s] = (hue, sat, val)

# HSV → BGR 변환
hist_color = cv2.cvtColor(hist_color_hsv, cv2.COLOR_HSV2BGR)

# 결과 영상 크기: 480 x 300
hist_color = cv2.resize(
    hist_color,
    (480, 300),
    interpolation=cv2.INTER_NEAREST
)

cv2.imshow("image", image)
cv2.moveWindow("image", 0, 0)
cv2.imshow("dst", hist_color)

cv2.waitKey(0)
cv2.destroyAllWindows()