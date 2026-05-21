import numpy as np, cv2, math
import scipy.fftpack as sf

def cos(n, k, N):
    return math.cos((n + 1 / 2) * math.pi * k / N)

def C(k, N):
    return math.sqrt(1 / N) if k == 0 else math.sqrt(2 / N)

def dct_1d(g):
    N = len(g)
    f = [
        C(k, N) * sum(g[n] * cos(n, k, N) for n in range(N))
        for k in range(N)
    ]
    return np.array(f, np.float32)

def idct_1d(F):
    N = len(F)
    g = [
        sum(C(k, N) * F[k] * cos(n, k, N) for k in range(N))
        for n in range(N)
    ]
    return np.array(g, np.float32)

def dct2_user(image):
    tmp = [dct_1d(row) for row in image]
    dst = [dct_1d(row) for row in np.transpose(tmp)]
    return np.transpose(dst)

def idct2_user(image):
    tmp = [idct_1d(row) for row in image]
    dst = [idct_1d(row) for row in np.transpose(tmp)]
    return np.transpose(dst)

def scipy_dct2(a):
    tmp = sf.dct(a, axis=0, norm='ortho')
    return sf.dct(tmp, axis=1, norm='ortho')

def scipy_idct2(a):
    tmp = sf.idct(a, axis=0, norm='ortho')
    return sf.idct(tmp, axis=1, norm='ortho')

# OpenCV DCT는 홀수 크기를 지원하지 않으므로 짝수 크기 사용
block = np.zeros((8, 8), np.uint8)
cv2.randn(block, 128, 50)

dct_user = dct2_user(block)
dct_scipy1 = scipy_dct2(block)
dct_scipy2 = sf.dctn(block, shape=block.shape, norm='ortho')
dct_opencv = cv2.dct(block.astype(np.float32))

idct_user = idct2_user(dct_user)
idct_scipy1 = scipy_idct2(dct_scipy1)
idct_scipy2 = sf.idctn(dct_scipy2, shape=dct_scipy2.shape, norm='ortho')
idct_opencv = cv2.dct(dct_opencv, flags=cv2.DCT_INVERSE)

print("block=\n", block)

print("dct_user(저자구현함수)=\n", dct_user)
print("dct_scipy1(scipy 모듈 함수1)=\n", dct_scipy1)
print("dct_scipy2(scipy 모듈 함수2)=\n", dct_scipy2)
print("dct_opencv(OpenCV 함수)=\n", dct_opencv)

print()
print("idct_user(저자구현함수)=\n", cv2.convertScaleAbs(idct_user))
print("idct_scipy1(scipy 모듈 함수1)=\n", cv2.convertScaleAbs(idct_scipy1))
print("idct_scipy2(scipy 모듈 함수2)=\n", cv2.convertScaleAbs(idct_scipy2))
print("idct_opencv(OpenCV 함수)=\n", cv2.convertScaleAbs(idct_opencv))