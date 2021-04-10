# ROI(Region of Interest: 관심 있는 영역) 추출
import cv2

image = cv2.imread('cat.jpg')

# Numpy Slicing: ROI 처리 가능
roi = image[200:350, 50:200]

# ROI 단위로 이미지 복사하기
image[0:150, 0:150] = roi

cv2.imshow('Image Basic', image)#사진 출력
cv2.waitKey(0)#창이 닫히지 않도록 하는것

