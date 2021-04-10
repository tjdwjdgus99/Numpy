#이미지 흑백ret, thres1 = cv2.threshold(image,127, 255, cv2.THRESH_BINARY) 구분
import  cv2

image = cv2.imread('2.jpg' ,cv2.IMREAD_GRAYSCALE)#그레이 색으로 입력 받은

ret, thres1 = cv2.threshold(image,127, 255, cv2.THRESH_BINARY)
thres2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,3)

cv2.imshow('Image Basic', image)#사진 출력
cv2.waitKey(0)  # 창이 닫히지 않도록 하는것

cv2.imshow('Image Basic', thres1)#그냥 흑백 나누기
cv2.waitKey(0)  # 창이 닫히지 않도록 하는것

cv2.imshow('Image Basic', thres2)#필터를 넣어 흑백 나누기
cv2.waitKey(0)  # 창이 닫히지 않도록 하는것