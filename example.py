import numpy as np

list_data = [1 , 2 , 3]
array = np.array(list_data)

print(array)
print(array.size)
print(array.dtype)
print(array[2])
print("---------------")

# 0 부터 3까지의 배열 만들기
array1 = np.arange(4)
print(array1)

#각 데이터가 0으로 초기화 했으면 좋겠다 4 X 4 크기로
array2 = np.zeros((4,4), dtype=float)
print(array2)
print("---------------")

#1로 초기화 시키고 싶다 3 X 3크기로
array3=np.ones((3,3),dtype=str)
print(array3)
print("---------------")

#0부터 9까지 랜덤하게 초기화된 배열 3 X 3 크기로
array4 = np.random.randint(0,10,(3,3))
print(array4)
print("---------------")

#평균이 0이고 표준편차가 1인 표준 정규를 뛰는 배열
array5 = np.random.normal(0 , 1 ,(3 , 3))
print(array5)