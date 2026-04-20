# 3행, 6열의 행렬을 생성하고, 행렬의 원소를 초기화한 후에 cv2.reduce() 함수를 이용해서 가로 방향과 세로 방향으로 감축하여 평균을 구한 결과를 출력하시오.

import numpy as np, cv2

arr = np.random.rand(3,6)
print(arr)
print()

avg1 = cv2.reduce(arr, 0, cv2.REDUCE_AVG) # 열 방향 연산, 1행으로 축소
print("열 방향 연산, 1행으로 축소")
print(avg1)
print()

avg2 = cv2.reduce(arr, 1, cv2.REDUCE_AVG) # 행 방향 연산, 1열으로 축소
print("행 방향 연산, 1열으로 축소")
print(avg2)
print()