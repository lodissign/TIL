# 0708.py
import cv2
import numpy as np

#1
src = np.full((512,512,3), (255, 255, 255), dtype= np.uint8)    # 515x515 크기의 배경이 하얀색인 3-채널 컬러 영상 src 생성.
cv2.rectangle(src, (50, 50), (200, 200), (0, 0, 255), 2)    # 빨간색 사각형 그림.
cv2.circle(src, (300, 300), 100, (0,0,255), 2)  # 반지름 100인 빨간색 원 그림.

#2
dst = src.copy()    # 깊은 복사.
cv2.floodFill(dst, mask=None, seedPoint=(100,100), newVal=(255,0,0))    # seedPoint를 시작점으로 사각형 내부를 newVal 색상으로 dst에 채움.

#3
retval, dst2, mask, rect=cv2.floodFill(dst, mask=None,
                          seedPoint=(300,300), newVal=(0,255,0))
print('rect=', rect)
x, y, width, height = rect
cv2.rectangle(dst2, (x,y), (x+width, y+height), (255, 0, 0), 2)

cv2.imshow('src',  src)
cv2.imshow('dst',  dst)
cv2.waitKey()
cv2.destroyAllWindows()
