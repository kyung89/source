import numpy as np, cv2

m1 = np.array([[3, 6, 3], [-5, 6, 1], [2, -3, 5]], np.float32)
m2 = np.array([2, 10, 28], np.float32)

ret, dst = cv2.solve(m1, m2, flags=cv2.DECOMP_LU)
print(dst)