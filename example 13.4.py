#글자 쓰기
import cv2
import numpy as np

image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.putText(image, 'Hello World', (0, 200), cv2.FONT_ITALIC, 2, (255, 0, 0))
#                            쓸 단어         위치        글자체
cv2.imshow('Image', image)
cv2.waitKey(0)