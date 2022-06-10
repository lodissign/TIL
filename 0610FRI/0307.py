#0307.py
import cv2
import numpy as np

img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255

x, y = 100, 100
size = 100

# for angle in range(0, 90, 5):  # 5도씩 움직이며 18개의 사각형 생성.
for angle in range(0, 90, 1):
    rect = ((x, y), (size, size), angle)
    box = cv2.boxPoints(rect).astype(np.int32)  # 중심 (256,256), 크기(size,size), 각도 angle인 회전 사각형 rect의 모서리 점을 정수로 변환하여 box에 계산.
    r = np.random.randint(256)
    g = np.random.randint(256)
    b = np.random.randint(256)   
    # cv2.polylines(img, [box], True, (b, g, r), 2)   # 회전 사각형의 모서리 점을 닫힌 다각형을 난수로 생성한 (b,g,r) 색상으로 그린다. 
    cv2.polylines(img, [box], True, (0,0,0), 2)   # 검은색으로만 box 그리기.
    
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
