#픽셀별로 이미지 합치기
import cv2

image_1 = cv2.imread('1.jpg')#두 사진의 배열의 크기가 같아야 한다
image_2 = cv2.imread('2.jpg')#두 사진의 배열의 크기가 같아야 한다

result = cv2.add(image_1, image_2)#이게 더 자연스럽다
cv2.imshow('Image Basic', result)#사진 출력
cv2.waitKey(0)#창이 닫히지 않도록 하는것

result = image_1 + image_2#이건 조금 부자연 스럽다
cv2.imshow('Image Basic', result)#사진 출력
cv2.waitKey(0)#창이 닫히지 않도록 하는것
