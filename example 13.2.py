#원 그리기
import cv2
import numpy as np
#                512X 512 두께  색상
image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.circle(image, (255, 255), 30, (255, 0, 0), 3)
#                 좌표 어디부터 어디까지,반지름 ,R   G  V  두께
cv2.imshow('Image', image)
cv2.waitKey(0)