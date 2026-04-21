# 09. 실수형 원소 10개를 갖는 ndarray 행렬을 선언해서 전체 원소의 합과 평균을 구하시오. 합과 평균은 소수점 둘째 자리까지 나타내시오.

import numpy as np

np.random.seed(10)
arr = np.random.rand(10)
print("arr = \n", arr)
print()

print("전체 원소의 합: ", round(np.sum(arr), 2))
print("전체 원소의 평균: ", round(np.mean(arr), 2))