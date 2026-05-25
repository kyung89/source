# 컬러 영상을 입력받아서 YCbCr 컬러 공간으로 변환하고 다시 환원하는 프로그램을 작성하시오.
# 단, cv2.cvtColor() 함수를 사용하지 않고, YCbCr 변환 수식에 따라서 직접 구현하시오.

import numpy as np, cv2

def convertToYCbCr(bgr):
    bgr = bgr.astype(np.float32)

    B, G, R = cv2.split(bgr)

    Y  = 0.299 * R + 0.587 * G + 0.114 * B
    Cb = (B - Y) * 0.564 + 128
    Cr = (R - Y) * 0.713 + 128

    YCbCr = cv2.merge((Y, Cr, Cb))
    return np.clip(YCbCr, 0, 255).astype(np.uint8)

def convertToBGR(ycbcr):
    ycbcr = ycbcr.astype(np.float32)

    Y, Cr, Cb = cv2.split(ycbcr)

    B = Y + 1.773 * (Cb - 128)
    G = Y - 0.344 * (Cb - 128) - 0.714 * (Cr - 128)
    R = Y + 1.403 * (Cr - 128)

    BGR = cv2.merge((B, G, R))
    return np.clip(BGR, 0, 255).astype(np.uint8)

BGR_img = cv2.imread('../images/color_space.jpg', cv2.IMREAD_COLOR)
if BGR_img is None: raise Exception('BGR_img is None')

YCbCr_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2YCrCb)

convertToYCbCr_img = convertToYCbCr(BGR_img)
convertToBGR_img = convertToBGR(convertToYCbCr_img)

cv2.imshow("BGR_img", BGR_img)
cv2.imshow("YCbCr_img: openCV", YCbCr_img)

cv2.imshow("user function: to YCbCr", convertToYCbCr_img)
cv2.imshow("user function: to BGR", convertToBGR_img)

cv2.waitKey(0)