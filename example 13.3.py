#다각형 그리기
import cv2
import numpy as np

image = np.full((512, 512, 3), 255, np.uint8)
points = np.array([[5, 5], [128, 258], [483, 444], [400, 150]])
#네개의 점
image = cv2.polylines(image, [points], True, (0, 0, 255), 4)
#                                             ,R   G  V  두께

cv2.imshow('Image', image)
cv2.waitKey(0)