#이미지 크기및 픽셀 정보 확인
import cv2

image = cv2.imread('cat.jpg' , cv2.IMREAD_COLOR)
# 픽셀 수 및 이미지 크기 확인
print(image.shape)
print(image.size)

# 이미지 Numpy 객체의 특정 픽셀을 가리킵니다.
px = image[100, 100]#이미지 픽셀 404,599 를 넘으면 오류가 뜬다

# B, G, R 순서로 출력됩니다.
# (단, Gray Scale인 경우에는 B, G, R로 구분되지 않습니다.)
print(px)

# R 값만 출력하기
print(px[2])