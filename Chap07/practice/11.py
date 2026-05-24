# 1차 미분 연산을 수행하도록 마스크를 생성하여 직접 회선을 수행하시오(3가지 연산 마스크 적용)

import numpy as np, cv2

def filter(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)
    ycenter, xcenter = mask.shape[0]//2, mask.shape[1]//2

    for i in range(ycenter, rows - ycenter):
        for j in range(xcenter, cols - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1
            x1, x2 = j - xcenter, j + xcenter + 1
            roi = image[y1:y2, x1:x2].astype('float32')
            tmp = cv2.multiply(roi, mask)
            dst[i, j] = cv2.sumElems(tmp)[0]
    return dst

def differential(image, data1, data2):
    mask1 = np.array(data1, np.float32).reshape(3, 3)
    mask2 = np.array(data2, np.float32).reshape(3, 3)

    dst1 = filter(image, mask1)
    dst2 = filter(image, mask2)
    dst = cv2.magnitude(dst1, dst2)

    dst = cv2.convertScaleAbs(dst)
    dst1 = cv2.convertScaleAbs(dst1)
    dst2 = cv2.convertScaleAbs(dst2)
    return dst, dst1, dst2

image = cv2.imread("../images/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

roberts_data1 = [-1, 0, 0, 0, 1, 0, 0, 0, 0]
roberts_data2 = [0, 0, -1, 0, 1, 0, 0, 0, 0]

prewitt_data1 = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
prewitt_data2 = [-1, -1, -1, 0, 0, 0, 1, 1, 1]

sobel_data1 = [-1, 0, 1, -2, 0, 2, -1, 0, 1]
sobel_data2 = [-1, -2, -1, 0, 0, 0, 1, 2, 1]

roberts_dst, roberts_dst1, roberts_dst2 = differential(image, roberts_data1, roberts_data2)
prewitt_dst, prewitt_dst1, prewitt_dst2 = differential(image, prewitt_data1, prewitt_data2)
sobel_dst, sobel_dst1, sobel_dst2 = differential(image, sobel_data1, sobel_data2)

cv2.imshow("image", image)
cv2.imshow("roberts edge", roberts_dst)
cv2.imshow("prewitt edge", prewitt_dst)
cv2.imshow("sobel edge", sobel_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()