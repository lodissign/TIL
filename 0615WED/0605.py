# 0605.py
import cv2
import numpy as np

# #1
src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
blur= cv2.GaussianBlur(src, ksize=(7, 7), sigmaX=0.0)   # 입력 영상 src를 부드럽게 하여 미분 오차를 줄이기 위하여 ksize=(7,7) 크기의 필터를 사용한 가우시안 블러링으로 blur 생성.
# cv2.imshow('src',  src)
# cv2.imshow('blur', blur)

# #2
# lap  = cv2.Laplacian(src, cv2.CV_32F)   # 입력 영상 src에 라플라시안 필터링하여 lap 생성.
# minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(lap)
# print('lap:', minVal, maxVal, minLoc, maxLoc)
# dst = cv2.convertScaleAbs(lap)
# dst = cv2.normalize(dst, None, 0, 255, cv2.NORM_MINMAX)
# cv2.imshow('lap',  lap)
# cv2.imshow('dst',  dst)

#3
lap2 = cv2.Laplacian(blur, cv2.CV_32F)  # blur 처리 된 영상으로 라플라시안 필터링.
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(lap2)
print('lap2:', minVal, maxVal, minLoc, maxLoc)
dst2 = cv2.convertScaleAbs(lap2)
dst2 = cv2.normalize(dst2, None, 0, 255, cv2.NORM_MINMAX)

cv2.imshow('lap2',  lap2)
cv2.imshow('dst2',  dst2)

cv2.waitKey()    
cv2.destroyAllWindows()
