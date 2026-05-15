import numpy as np, math, cv2, time

def scaling(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    y = np.arange(0, img.shape[0], 1)
    x = np.arange(0, img.shape[1], 1)
    y, x = np.meshgrid(y, x)
    i, j = np.int32(y * ratioY), np.int32(x * ratioX)
    dst[i, j] = img[y, x]
    return dst

def scaling_nearest(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    i = np.arange(0, size[1], 1)
    j = np.arange(0, size[0], 1)
    i, j = np.meshgrid(i, j)
    y, x = np.int32(i / ratioY), np.int32(j / ratioX)
    dst[i, j] = img[y, x]
    return dst

def bilinear_value(img, pt):
    x, y = np.int32(pt)
    if x >= img.shape[1]-1: x = x - 1
    if y >= img.shape[0]-1: y = y - 1
    P1, P2, P3, P4 = np.float32(img[y:y+2, x:x+2].flatten())
    ## 4개 화소 - 화소 직접 접근
    # P1 = float(img[y, x])
    # P2 = float(img[y + 0, x + 1])
    # P3 = float(img[y + 1, x + 0])
    # P4 = float(img[y + 1, x + 1])

    alpha, beta = pt[1] - y, pt[0] - x
    M1 = P1 + alpha * (P3 - P1)
    M2 = P2 + alpha * (P4 - P2)
    P = M1 + beta * (M2 - M1)
    return np.clip(P, 0, 255)

def scaling_bilinear(img, size):
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])

    dst = [[bilinear_value(img, (j/ratioX, i/ratioY)) for j in range(size[0])] for i in range(size[1])]
    return np.array(dst, img.dtype)

def contain(p, shape):
    return 0 <= p[0] < shape[0] and 0 <= p[1] < shape[1]


def rotate(img, degree):
    dst = np.zeros(img.shape[:2], img.dtype)
    radian = (degree / 180) * np.pi
    sin, cos = np.sin(radian), np.cos(radian)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            y = -j * sin + i * cos
            x = j * cos + i * sin
            if contain((y, x), img.shape):
                dst[i, j] = bilinear_value(img, [x, y])
    return dst

def rotate_pt(img, degree, pt):
    dst = np.zeros(img.shape[:2], img.dtype)
    radian = (degree / 180) * np.pi
    sin, cos = math.sin(radian), math.cos(radian)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            jj, ii = np.subtract((j, i), pt)
            y = -jj * sin + ii * cos
            x = jj * cos + ii * sin
            x, y = np.add((x, y), pt)
            if contain((y, x), img.shape):
                dst[i, j] = bilinear_value(img, (x, y))
    return dst