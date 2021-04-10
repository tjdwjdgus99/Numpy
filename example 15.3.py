#면적 둘레 특징 구하기
import cv2

image = cv2.imread('digit_image.jpg')
image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)#이미지 줄이기
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 230, 255, 0)
thresh = cv2.bitwise_not(thresh)

contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
image = cv2.drawContours(image, contours, -1, (0, 0, 255), 4)

contour = contours[0]
area = cv2.contourArea(contour)#면적구하기
print(area)

length = cv2.arcLength(contour, True)#둘레구하기
print(length)

M = cv2.moments(contour)#특징 추출하기
print(M)

cv2.imshow('Image', image)
cv2.waitKey(0)