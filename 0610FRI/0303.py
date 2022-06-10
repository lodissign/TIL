#0303.py
import cv2
import numpy as np

img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
cy = img.shape[0]//2
cx = img.shape[1]//2
# cx, cy에 영상의 중심을 정수로 계산.

for r in range(200, 0, -100):   # for 문으로 원의 반지름 r을 200, 100으로 반복하면서, 
    cv2.circle(img, (cx, cy), r, color=(255, 0, 0)) # cv2.circle() 함수로 원의 중심 (cx, cy), 반지름 r, 색상 (255,0,0)인 파란색 원을 그린다.

cv2.circle(img, (cx, cy), radius=50, color=(0, 0, 255), thickness=-1)   # cv2.circle() 함수로 thickness=-1 로 하여 빨간색 원을 그린다. 

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
