# 10. 0~50 사이의 임의의 원소(정수형, 중복가능)를 500개 만들어서 가장 중복이 많이 나온 원소 3개를 원소값과 중복 횟수로 출력하시오.

import numpy as np

np.random.seed(10)
nums = np.random.randint(0, 51, 500)
print("nums = \n", nums)
print()

check = {}
for i in range(0, 51):
    check[i] = 0
for i in range(0, 51):
    check[nums[i]] += 1

top3 = sorted(check.items(), key=lambda x:x[1], reverse=True)[:3]
for top in top3:
    print("원소값: ", top[0], ", 중복횟수: ", top[1])