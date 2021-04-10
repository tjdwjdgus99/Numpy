#이미지 회전
import cv2

image = cv2.imread('cat.jpg')

# 행과 열 정보만 저장합니다.
height, width = image.shape[:2]
                # 회전의 중심값을 세로 절반 가로 절반,  회전각도,크기
M = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 0.5)#회전
dst = cv2.warpAffine(image, M, (width, height))#사진 넣어주기

cv2.imshow('Image Basic', dst)#사진 출력
cv2.waitKey(0)#창이 닫히지 않도록 하는것