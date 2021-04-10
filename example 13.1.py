#네모 그리기
import cv2
import numpy as np
#                512X 512 두께  색상
image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.rectangle(image, (20, 20), (255, 255), (255, 0, 0), -1)
#                           좌표 어디부터  어디까지      R   G  V  두께

cv2.imshow('Image', image)
cv2.waitKey(0)