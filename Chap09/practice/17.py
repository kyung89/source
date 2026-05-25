# 다시 풀이

# OpenCV의 cv2.dct() 함수를 이용해서 8 x 8 블록으로 DCT와 IDCT를 수행하는 프로그램을 작성하시오.

import numpy as np
import cv2

def block_dct_idct(image, block_size=8):
    h, w = image.shape[:2]

    # 8의 배수 크기만 처리
    h8 = h - (h % block_size)
    w8 = w - (w % block_size)

    src = image[:h8, :w8].astype(np.float32)

    dct_img = np.zeros((h8, w8), np.float32)
    idct_img = np.zeros((h8, w8), np.float32)

    for y in range(0, h8, block_size):
        for x in range(0, w8, block_size):
            block = src[y:y+block_size, x:x+block_size]

            # DCT
            dct_block = cv2.dct(block)

            # IDCT
            idct_block = cv2.dct(dct_block, flags=cv2.DCT_INVERSE)

            dct_img[y:y+block_size, x:x+block_size] = dct_block
            idct_img[y:y+block_size, x:x+block_size] = idct_block

    return dct_img, cv2.convertScaleAbs(idct_img)

image = cv2.imread("../images/dct.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상파일 읽기 에러")

dct_img, idct_img = block_dct_idct(image, 8)

# DCT 계수는 보기 좋게 로그 변환
dct_show = np.log(np.abs(dct_img) + 1)
dct_show = cv2.normalize(dct_show, None, 0, 255, cv2.NORM_MINMAX)
dct_show = dct_show.astype(np.uint8)

cv2.imshow("image", image)
cv2.imshow("8x8 DCT", dct_show)
cv2.imshow("8x8 IDCT", idct_img)

cv2.waitKey(0)
cv2.destroyAllWindows()