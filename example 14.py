#테두리 안에있는 글자 찾기
import cv2

image = cv2.imread('2.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 127, 255, 0)

cv2.imshow('Image', thresh)
cv2.waitKey(0)

#1) RETR_EXTERNAL: 바깥쪽 Line만 찾기
#2) RETR_LIST: 모든 Line을 찾지만, Hierarchy 구성 X
#3) RETR_TREE: 모든 Line을 찾으며, 모든 Hierarchy 구성 O
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
image = cv2.drawContours(image, contours, -1, (0, 255, 0), 4)
#                                         -1은 전체를 뜻함

cv2.imshow('Image', image)
cv2.waitKey(0)