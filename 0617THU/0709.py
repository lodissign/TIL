# 0709.py
import cv2
import numpy as np

#1
src = np.zeros(shape=(512,512), dtype=np.uint8)
cv2.rectangle(src, (50, 200), (450, 300), (255, 255, 255), -1)

#2
dist  = cv2.distanceTransform(src, distanceType=cv2.DIST_L1, maskSize=3)    # dist에 거리 계산.
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(dist)    # maxVal=51.0
print('src:', minVal, maxVal, minLoc, maxLoc)

dst = cv2.normalize(dist, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)   # dist를 [0,255] 범위로 정규화.
ret, dst2 = cv2.threshold(dist, maxVal-1, 255, cv2.THRESH_BINARY)   # dist를 maxVal-1, binary로 임계값 영상 생성.

#3 
gx = cv2.Sobel(dist, cv2.CV_32F, 1, 0, ksize = 3)   # Sobel필터로 거리 dist에서 그래디언트 계산.
gy = cv2.Sobel(dist, cv2.CV_32F, 0, 1, ksize = 3)
mag   = cv2.magnitude(gx, gy)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(mag)
print('src:', minVal, maxVal, minLoc, maxLoc)
ret, dst3 = cv2.threshold(mag, maxVal-2, 255, cv2.THRESH_BINARY_INV)    # mag를 maxVal-1, binary_inv로  임계값 영상 생성.

cv2.imshow('src',  src)
cv2.imshow('dst',  dst)
cv2.imshow('dst2',  dst2)
cv2.imshow('dst3',  dst3)
cv2.waitKey()
cv2.destroyAllWindows()
