import numpy as np, cv2

alpha = 0.5
beta = 0.5

def changeAlpha(value):
    alpha = value * 0.01
    image3 = cv2.addWeighted(image1, alpha, image2, beta, 0)
    result = cv2.hconcat([image1, image3, image2])
    cv2.imshow('image', result)

def changeBeta(value):
    beta = value * 0.01
    image3 = cv2.addWeighted(image1, alpha, image2, beta, 0)
    result = cv2.hconcat([image1, image3, image2])
    cv2.imshow('image', result)

image1 = cv2.imread('images/add1.jpg')
image2 = cv2.imread('images/add2.jpg')

image3 = cv2.addWeighted(image1, alpha, image2, beta, 0)

concat = cv2.hconcat([image1, image3, image2])
cv2.imshow('image', concat)

cv2.createTrackbar("alpha[%]", "image", 50, 100, changeAlpha)
cv2.createTrackbar("beta[%]", "image", 50, 100, changeBeta)

cv2.waitKey(0)
cv2.destroyAllWindows()