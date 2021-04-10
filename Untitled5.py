import numpy as np

#2 2크기로 1 부터 10까지 10을 곱한 수
array = np.random.randint(1,10,(2,2))
print(array * 10)

#            총 갯수       nXn을 표현
array1 = np.arange(4).reshape(2,2)
array2 = np.arange(2).reshape(1,2) #비여있는 부분은 위를 복사해 아래에 붙이는 방식이다

array3 = array1 + array2
print(array3)
print("---------------")

#                총 갯수      2X4형태
array4 = np.arange(0 , 8).reshape(2,4)
array5 = np.arange(0 , 8).reshape(2,4)
array6 = np.concatenate([array4, array5], axis=0)

print(array6)