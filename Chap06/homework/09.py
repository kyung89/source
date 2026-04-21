# 8번 문제에 두 개의 트랙바를 추가해서 각 영상의 반영 비율을 조절할 수 있도록 수정하시오.

import numpy as np, cv2

image1 = cv2.imread('add1.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('add2.jpg', cv2.IMREAD_GRAYSCALE)

alpha, beta = 0.5, 0.5
image3 = cv2.addWeighted(image1, alpha, image2, beta, 0)
merged = cv2.hconcat([image1, image3, image2])

# cv2.imshow('image1', image1)
# cv2.imshow('image2', image2)
# cv2.imshow('image3', image3)
# cv2.imshow('dst', merged)

def setAlpha(value):
    global alpha
    alpha = value * 0.01
    image3 = cv2.addWeighted(image1, alpha, image2, beta, 0)
    merged = cv2.hconcat([image1, image3, image2])
    cv2.imshow('dst', merged)

def setBeta(value):
    global beta
    beta = value * 0.01
    image3 = cv2.addWeighted(image1, alpha, image2, beta, 0)
    merged = cv2.hconcat([image1, image3, image2])
    cv2.imshow('dst', merged)

cv2.namedWindow('dst')
cv2.imshow('dst', merged)

cv2.createTrackbar("alpha(%)", "dst", 50, 100, setAlpha)
cv2.createTrackbar("beta(%)", "dst", 50, 100, setBeta)

cv2.waitKey(0)