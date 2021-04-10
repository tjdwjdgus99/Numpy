#이미지 크기조절
import cv2
#원본
image = cv2.imread('cat.jpg')
cv2.imshow('Image Basic', image)#사진 출력
cv2.waitKey(0)#창이 닫히지 않도록 하는것
#키우기
expand = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Image Basic', expand)#사진 출력
cv2.waitKey(0)#창이 닫히지 않도록 하는것
#줄이기
shrink = cv2.resize(image, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA)
cv2.imshow('Image Basic', shrink)#사진 출력
cv2.waitKey(0)#창이 닫히지 않도록 하는것