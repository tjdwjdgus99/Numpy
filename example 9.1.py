#이미지 위치이동
import cv2

image = cv2.imread('cat.jpg')

# 행과 열 정보만 저장합니다.
height, width = image.shape[:2]
        #1 , 0은 고정 가로라는 뜻 그다음 이동할 값 그다음은 세로
M = np.float32([[1, 0, 100], [0, 1, 10]])#사진이동
dst = cv2.warpAffine(image, M, (width, height))#사진넣어주기

cv2.imshow('Image Basic', dst)#사진 출력
cv2.waitKey(0)#창이 닫히지 않도록 하는것