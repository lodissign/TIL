# 0516.py
import cv2
import numpy as np 
#1
src = cv2.imread('./data/tsukuba_l.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('src', src)  # 대부분의 배경이 어둡고 조각상의 얼굴만 밝은 영상.

#2
dst = cv2.equalizeHist(src) # 전체 영상에 대해 하나의 히스토그램을 이용하여 dst에 평활화.
cv2.imshow('dst', dst)  # 영상 전체가 밝아져서 얼굴 부분의 윤곽선이 구분되지 않음.

#3
clahe2 = cv2.createCLAHE(clipLimit=40, tileGridSize=(1,1))  # 하나의 히스토그램만을 가지고, 
dst2 = clahe2.apply(src)    # CLAHE 히스토그램 평활화.
cv2.imshow('dst2', dst2)    # 하나의 히스토그램을 사용하기 때문에 dst와 비슷한 결과.

#4
clahe3 = cv2.createCLAHE(clipLimit=40, tileGridSize=(8,8))  # 타일로 나누어 평활화.
dst3 = clahe3.apply(src)
cv2.imshow('dst3', dst3)    # dst, dst2에 비해 대비가 선명한 영상.

cv2.waitKey()    
cv2.destroyAllWindows()
