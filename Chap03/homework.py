import numpy as np

# 9. 실수형 원소10개를 갖는 narray 행렬을 선언해서 전체 원소의 합과 평균을 구하시오. 합과 평균은 소수점 둘째자리까지 나타내시오.

print()
print("9. 실수형 원소10개를 갖는 narray 행렬을 선언해서 전체 원소의 합과 평균을 구하시오. 합과 평균은 소수점 둘째자리까지 나타내시오.")
print()

import numpy as np

np.random.seed(10)
arr1 = np.random.rand(10)
print(arr1), print()
print(type(arr1[0])), print()
print("전체 원소의 합: ", round(np.sum(arr1), 2))
print("전체 원소의 평균: ", round(np.mean(arr1), 2))
print()

# 10. 0~50 사이의 임의의 원소(정수형, 중복가능)를 500개를 만들어서 가장 중복이 많이 나온 원소 3개를 원소값과 중복횟수로 출력하시오.

print()
print("10. 0~50 사이의 임의의 원소(정수형, 중복가능)를 500개를 만들어서 가장 중복이 많이 나온 원소 3개를 원소값과 중복횟수로 출력하시오.")
print()

import numpy as np

arr2 = np.random.randint(0, 51, 500)
print(arr2)
print()

check = {}
for i in range(0, 51):
    check[i] = 0
for i in arr2:
    check[i] += 1
#print(check)
#print()

top3 = sorted(check.items(), key=lambda x: x[1], reverse=True)[:3]
for key, value in top3 :
    print("원소값: ", key, ", 중복횟수: ", value)