import numpy as np

array1 = np.arange(16).reshape(4,4)
print(array1)

array2 = array1 < 10
print(array2)

array1[array2] = 100#10보다 작은걸 100으로 바꾸기
print(array1)
print("---------------")

array = np.arange(16).reshape(4,4)

print("최대값: ", np.max(array))
print("최소값: ", np.min(array))
print("합계: ", np.sum(array))
print("평균값: ", np.mean(array))

print("합계: ", np.sum(array, axis=0))#열단위로 모두 합해서 출력