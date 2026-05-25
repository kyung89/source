import numpy as np, math, cv2

def contain(p, shape):
    return 0 <= p[0] < shape[0] and 0 <= p[1] < shape[1]

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

image = cv2.imread("../images/rotate.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

h, w = image.shape[:2]
center = (100, 100)
angle = -30
scale = 1

dst1 = rotate_pt(image, 30, center)

rot_mat = cv2.getRotationMatrix2D(center, angle, scale)
dst2 = cv2.warpAffine(image, rot_mat, (w, h), flags=cv2.INTER_LINEAR)

cv2.imshow("image", image)
cv2.imshow("dst1 : rotation() function", dst1)
cv2.imshow("dst2 : Affine Matrix", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()