#이미지 불러오기및 저장
import cv2
img_basic = cv2.imread('cat.jpg' , cv2.IMREAD_COLOR)
cv2.imshow('Image Basic', img_basic)
cv2.waitKey(0)#창이 닫히지 않도록 하는것
cv2.imwrite('result1.png',img_basic)#이미지 저장

cv2.destroyAllWindows()#닫고 다음걸로 나아감

img_gray = cv2.cvtColor(img_basic,cv2.COLOR_BGR2GRAY)#그래이 색으로
cv2.imshow('Image Gray', img_gray)
cv2.waitKey(0)#창이 닫히지 않도록 하는것
cv2.imwrite('result2.png',img_gray)