#이미지 임계점 처리하기
import  cv2

image = cv2.imread('2.jpg' ,cv2.IMREAD_GRAYSCALE)#그레이 색으로 입력 받은

images = []
ret, thres1 = cv2.threshold(image,127, 255, cv2.THRESH_BINARY)#127 이상이면 백색 아니면 흑색
ret, thres2 = cv2.threshold(image,127, 255, cv2.THRESH_BINARY_INV)#반대로
ret, thres3 = cv2.threshold(image,127, 255, cv2.THRESH_TRUNC)#127 이상은 다 127로
ret, thres4 = cv2.threshold(image,127, 255, cv2.THRESH_TOZERO)#127 보다 작으면 0으로
ret, thres5 = cv2.threshold(image,127, 255, cv2.THRESH_TOZERO_INV)#반대로
images.append(thres1)
images.append(thres2)
images.append(thres3)
images.append(thres4)
images.append(thres5)

for i in images:
    cv2.imshow('Image Basic', i)#사진 출력
    cv2.waitKey(0)  # 창이 닫히지 않도록 하는것