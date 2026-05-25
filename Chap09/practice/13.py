# 다시 풀이

# 주파수 영역 필터링에서 중간 주파수 대역만을 통과시키도록 필터를 생성해서 필터링을 수행하는 프로그램을 작성하시오.

import numpy as np
import cv2

def calc_spectrum(complex):
    mag = cv2.magnitude(complex[:, :, 0],
                        complex[:, :, 1])

    spectrum = 20 * np.log(mag + 1)

    return cv2.convertScaleAbs(spectrum)

image = cv2.imread("../images/filter.jpg",
                   cv2.IMREAD_GRAYSCALE)

if image is None:
    raise Exception("영상파일 읽기 에러")

rows, cols = image.shape
cy, cx = rows // 2, cols // 2

# FFT
dft = cv2.dft(np.float32(image),
              flags=cv2.DFT_COMPLEX_OUTPUT)

# 중심 이동
dft_shift = np.fft.fftshift(dft)

# -------------------------
# Band Pass Filter 생성
# -------------------------

mask = np.zeros((rows, cols, 2), np.float32)

inner_radius = 30
outer_radius = 80

for y in range(rows):
    for x in range(cols):

        dist = np.sqrt((y - cy)**2 +
                       (x - cx)**2)

        # 중간 주파수만 통과
        if inner_radius < dist < outer_radius:
            mask[y, x] = 1

# 필터링
filtered_dft = dft_shift * mask

# 스펙트럼
spectrum1 = calc_spectrum(dft_shift)
spectrum2 = calc_spectrum(filtered_dft)

# 중심 복원
idft_shift = np.fft.ifftshift(filtered_dft)

# IFFT
result = cv2.idft(idft_shift,
                  flags=cv2.DFT_SCALE |
                        cv2.DFT_REAL_OUTPUT)

result = cv2.convertScaleAbs(result)

cv2.imshow("image", image)
cv2.imshow("spectrum original", spectrum1)
cv2.imshow("band pass mask",
           mask[:, :, 0] * 255)
cv2.imshow("spectrum filtered", spectrum2)
cv2.imshow("result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()