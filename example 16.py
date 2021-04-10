#직접 커널을 사용하여 픽터적용하기
import cv2
import numpy as np

image = cv2.imread('2.jpg')
cv2.imshow('Image', image)
cv2.waitKey(0)

size = 4#커질수록 블러링이 강해진다
kernel = np.ones((size, size), np.float32) / (size ** 2) # 4 x 4 크기로 16으로 나누어준다
print(kernel)

dst = cv2.filter2D(image, -1, kernel)#1.수동으로 필터
cv2.imshow('Image', dst)
cv2.waitKey(0)

dst = cv2.blur(image, (4, 4))#2.자동으로 필터해 주는것
cv2.imshow('Image', dst)
cv2.waitKey(0)

dst = cv2.GaussianBlur(image, (5, 5), 0)#3.홀수로 필터
cv2.imshow('Image', dst)
cv2.waitKey(0)