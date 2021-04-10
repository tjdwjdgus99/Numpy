import numpy as np

array1 = np.array(([1, 2 , 3]))
array2 = np.array(([4, 5 , 6]))
array3 = np.concatenate([array1, array2])

print(array3.shape)#크기 (데이터 갯수)
print(array3)
print("---------------")
#2칸 2칸씩 만들기
array5 = np.array([1,2,3,4])
array6 = array5.reshape((2,2))
print(array6)
print("---------------")
#가로축을 기준으로 맞추기
array7 = np.arange(4).reshape(1,4)
array8 = np.arange(8).reshape(2,4)
print(array8)
print("---------------")
#세로축을 기준으로 맞추기
array8=np.concatenate([array7,array8],axis=0)
print(array8)
print("---------------")
#좌 우를 기준으로 2개2개 나누기
array10 = np.arange(8).reshape(2, 4)
left, right = np.split(array10, [2], axis=1)
print(left.shape)
print(right.shape)
print(array10)
print(left)