import numpy as np
import cv2

image = cv2.imread("../images/hue_hist.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상파일 읽기 에러")

# 이진화
_, binary = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)

# 수직 방향 투영
# 각 열(column)의 픽셀값 합
vertical = cv2.reduce(binary, 0, cv2.REDUCE_SUM, dtype=cv2.CV_32S)

# 수평 방향 투영
# 각 행(row)의 픽셀값 합
horizontal = cv2.reduce(binary, 1, cv2.REDUCE_SUM, dtype=cv2.CV_32S)

print("vertical shape:", vertical.shape)      # (1, width)
print("horizontal shape:", horizontal.shape)  # (height, 1)

# 시각화용 정규화
vertical_norm = cv2.normalize(vertical, None, 0, 255, cv2.NORM_MINMAX)
horizontal_norm = cv2.normalize(horizontal, None, 0, 255, cv2.NORM_MINMAX)

vertical_norm = vertical_norm.astype(np.uint8)
horizontal_norm = horizontal_norm.astype(np.uint8)

# 투영 그래프 영상 생성
h, w = binary.shape

vertical_img = np.full((200, w), 255, np.uint8)
horizontal_img = np.full((h, 200), 255, np.uint8)

# 수직 투영 그래프 그리기
for x in range(w):
    value = int(vertical_norm[0, x])
    cv2.line(vertical_img, (x, 199), (x, 199 - value), 0, 1)

# 수평 투영 그래프 그리기
for y in range(h):
    value = int(horizontal_norm[y, 0])
    cv2.line(horizontal_img, (0, y), (value, y), 0, 1)

cv2.imshow("image", image)
cv2.imshow("binary", binary)
cv2.imshow("vertical projection", vertical_img)
cv2.imshow("horizontal projection", horizontal_img)

cv2.waitKey(0)
cv2.destroyAllWindows()