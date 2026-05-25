# 다시 풀이

# 2의 자승 크기가 아닌 영상에 FFT를 수행하여 주파수 스펙트럼 영상을 출력하시오.

import numpy as np, cv2

def calc_spectrum(complex):
    if complex.ndim == 2: dst = abs(complex)                   # sqrt(re^2 + im^2) 계산해줌
    else: dst = cv2.magnitude(complex[:,:,0], complex[:,:,1])
    dst = 20*np.log(dst+1)
    return cv2.convertScaleAbs(dst)


def fftshift(img):
    dst = np.zeros(img.shape, img.dtype)
    h, w = dst.shape[:2]
    cy, cx = h // 2, w // 2                                     # 나누기 하며 소수점 절삭
    dst[h-cy:, w-cx:] = np.copy(img[0:cy , 0:cx ])      # 1사분면 -> 3사분면
    dst[0:cy, 0:cx ] = np.copy(img[h-cy:, w-cx:])      # 3사분면 -> 1사분면
    dst[0:cy, w-cx:] = np.copy(img[h-cy:, 0:cx ])      # 2사분면 -> 4사분면
    dst[h-cy:, 0:cx ] = np.copy(img[0:cy , w-cx:])      # 4사분면 -> 2사분면
    return dst

image = cv2.imread('../images/dft_240.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
spectrum = calc_spectrum(fftshift(dft))

cv2.imshow("spectrum", spectrum)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()