#특정 범위 픽셀 변경
import cv2
import time

image = cv2.imread('cat.jpg')
#첫번째 구역을 일일히 정하기
start_time = time.time()
for i in range(0, 100):
    for j in range(0, 100):
        image[i, j] = [255, 255, 255]
print("--- %s seconds ---" % (time.time() - start_time))#느림

#두번째 범위를 지정하기
start_time = time.time()
image[0:100, 0:100] = [0, 0, 0]
print("--- %s seconds ---" % (time.time() - start_time))#빠름

cv2.imshow('Image Basic', image)#사진 출력
cv2.waitKey(0)#창이 닫히지 않도록 하는것

