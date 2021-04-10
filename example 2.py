import numpy as np

#단일 객체 저장및 불러오기
array = np.arange(0 , 10)
np.save('saved.npy', array)

result = np.load('saved.npy')
print(result)

#복수 객체 저장및 불러오기
array1 = np.arange(0 , 10)
array2 = np.arange(10 , 20)
np.savez('saved.npz', array1=array1,array2=array2)

data = np.load('saved.npz')
result1= data['array1']
result2= data['array2']
print(result1)
print(result2)
print("---------------")

#Numpy 원소 오름차순 정렬
array3 = np.array([5,3,1,9,10])
array3.sort()
print(array3)
print(array3[::-1])#내림차순
print("---------------")

#세로로 정렬
array4 = np.array([[5,3,1,9,10] , [3,4,5,6,7]])
print(array4)
array4.sort(axis=0)
print(array4)
print("---------------")

#균일한 간격으로 데이터 생성
array = np.linspace(0, 10 , 5)#처음값 마지막값 몇개
print(array)

#난수의 재열 실행마다 결과 동일
np.random.seed(7)#이문장을 쓰면 난수가 동일하게 나옴 빼면 랜덤
print(np.random.randint(0,10,(2,3)))

# 배열 겍체 복사
array1 = np.arange(0,10)
array2 = array1.copy()#이렇게 쓰지 않으면 하나만 객체를 바꾸어도 둘바 바뀌지 않는다
array[0] = 99 #객체를 바꾸어 보았다
print(array1)