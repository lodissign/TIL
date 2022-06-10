#0304.py
import cv2
import numpy as np

img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
ptCenter = img.shape[1]//2, img.shape[0]//2
size = 200,100

cv2.ellipse(img, ptCenter, size, 0, 0, 360, (255, 0, 0))    # 타원의 중심 ptCenter, 축의 절반 크기 size, 각도 angle 0, 시작 각도 0, 끝 각도 360, 파란색 타원을 그린다.
cv2.ellipse(img, ptCenter, size, 45, 0, 360, (0, 0, 255))   # 각도 45, 빨간색 타원.

box = (ptCenter, size, 0)  # 각도 0인 box.
cv2.ellipse(img, box,  (255, 0, 0), 5)  # box로 파란색, 두께 5인 타원을 그린다. 크기size는 타원의 바운딩 박스의 크기. 9라인 타원의 절반 크기.

box = (ptCenter, size, 45)
cv2.ellipse(img, box,  (0, 0, 255), 5)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
