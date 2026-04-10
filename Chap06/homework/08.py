# OpenCV 함수 중에서 cv2.addWeighted() 함수를 사용해서 두 영상을 합성하는 프로그램을 작성하시오.

import numpy as np, cv2

image1 = cv2.imread('add1.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('add2.jpg', cv2.IMREAD_GRAYSCALE)

image3 = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)
merged = cv2.hconcat([image1, image3, image2])

# cv2.imshow('image1', image1)
# cv2.imshow('image2', image2)
# cv2.imshow('image3', image3)
cv2.imshow('dst', merged)
cv2.waitKey(0)