# 캐니 에지 알고리즘에서 이중 임계값을 트랙바로 만들어서 두개의 임계값을 조절하여 에지를 검출하도록 프로그램을 작성하시오.

import numpy as np, cv2

th1 = 50
th2 = 100

def onTrackbarTh1(th):
    th1 = th
    ## 캐니 에지 검출
    canny = cv2.Canny(image, th1, th2)
    cv2.imshow("canny edge", canny)

def onTrackbarTh2(th):
    th2 = th
    ## 캐니 에지 검출
    canny = cv2.Canny(image, th1, th2)
    cv2.imshow("canny edge", canny)

image = cv2.imread("../images/cannay_tset.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

## 캐니 에지 검출
canny = cv2.Canny(image, th1, th2)

cv2.imshow("canny edge", canny)
cv2.createTrackbar("th1", "canny edge", th1, 255, onTrackbarTh1)
cv2.createTrackbar("th2", "canny edge", th2, 255, onTrackbarTh2)
cv2.waitKey(0)
cv2.destroyAllWindows()