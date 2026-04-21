import numpy as np, cv2

np.random.seed(10)
arr = np.random.rand(3, 6)
print(arr)
print()

avg0 = cv2.reduce(arr, 0, cv2.REDUCE_AVG)
avg1 = cv2.reduce(arr, 1, cv2.REDUCE_AVG)

print("세로 방향 감축")
print(avg0)
print()
print("가로 방향 감축")
print(avg1)