# 다음의 연립방정식을 가우시안 소거법의 역함수를 계산해서 해를 구하는 프로그램을 작성하시오. [한번 더 체크!]

import numpy as np, cv2

data = [3, 6, 3, -5, 6, 1, 2, -3, 5]
m1 = np.array(data, np.float32).reshape(3,3)
m2 = np.array([2, 10, 28], np.float32)

_, dst = cv2.solve(m1, m2, cv2.DECOMP_LU)
print("[dst] =", dst.flatten())