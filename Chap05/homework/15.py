# 5.6절에서 예제 5.6.2의 사각형 회전하기 예제를 확장하여 그 사각형의 중심점을 기준으로 45도 회전시키는 프로그램을 완성하시오.

import numpy as np, cv2

pts1 = np.array([(100, 100, 1), (400, 100, 1), (400, 250, 1), (100, 250, 1)], np.float32)

theta = 45 * np.pi / 180
m = np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]], np.float32)

delta = (pts1[2] - pts1[0])//2
center = pts1[0] + delta

t1 = np.eye(3, dtype=np.float32)
t2 = np.eye(3, dtype=np.float32)

t1[0, 2], t1[1, 2] = -center[0], -center[1]
t2[0, 2], t2[1, 2] =  center[0],  center[1]
m2 = t2 @ m @ t1

pts2 = cv2.gemm(pts1, m2, 1, None, 1, flags=cv2.GEMM_2_T)

for i, (pt1, pt2) in enumerate(zip(pts1, pts2)):
    print("pts1[%d] = %s, pts2[%d] = %s" % (i, pt1, i, pt2))

image = np.full((400, 500, 3), 255, np.uint8)
cv2.polylines(image, [np.int32(pts1[:, :2])], True, (0, 255, 0), 2)
cv2.polylines(image, [np.int32(pts2[:, :2])], True, (255, 0, 0), 3)
cv2.imshow("image", image)
cv2.waitKey(0)