#픽셀별 색상 다루기
import cv2

image = cv2.imread('cat.jpg')
image[:, :, 2] = 0#색상 바꾸기

cv2.imshow('Image Basic', image)#사진 출력
cv2.waitKey(0)#창이 닫히지 않도록 하는것