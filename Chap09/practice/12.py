# 다시 풀이

import numpy as np
import cv2

def calc_spectrum(complex):
    if complex.ndim == 2:
        dst = abs(complex)
    else:
        dst = cv2.magnitude(complex[:, :, 0], complex[:, :, 1])
    dst = 20 * np.log(dst + 1)
    return cv2.convertScaleAbs(dst)

def fftshift(img):
    dst = np.zeros(img.shape, img.dtype)
    h, w = dst.shape[:2]
    cy, cx = h // 2, w // 2

    dst[h-cy:, w-cx:] = np.copy(img[0:cy, 0:cx])
    dst[0:cy, 0:cx] = np.copy(img[h-cy:, w-cx:])
    dst[0:cy, w-cx:] = np.copy(img[h-cy:, 0:cx])
    dst[h-cy:, 0:cx] = np.copy(img[0:cy, w-cx:])

    return dst

image = cv2.imread('../images/dft_240.jpg', cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상파일 읽기 에러")

h, w = image.shape[:2]

# 2의 자승 크기 구하기
padded_h = cv2.getOptimalDFTSize(h)
padded_w = cv2.getOptimalDFTSize(w)

# 영삽입 영상 생성
padded = np.zeros((padded_h, padded_w), np.float32)
padded[:h, :w] = image.astype(np.float32)

# 영삽입된 영상으로 DFT
dft = cv2.dft(padded, flags=cv2.DFT_COMPLEX_OUTPUT)

# 스펙트럼
spectrum = calc_spectrum(fftshift(dft))

# 1. 영삽입이 있는 상태로 IFFT
idft_padded = cv2.idft(dft, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)

# 2. 영삽입 제거한 결과 영상
idft_removed = idft_padded[:h, :w]

cv2.imshow("image", image)
cv2.imshow("zero padded image", cv2.convertScaleAbs(padded))
cv2.imshow("spectrum", spectrum)

cv2.imshow("IFFT with zero padding", cv2.convertScaleAbs(idft_padded))
cv2.imshow("IFFT removed zero padding", cv2.convertScaleAbs(idft_removed))

cv2.waitKey(0)
cv2.destroyAllWindows()