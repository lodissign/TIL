# 0418.py: OpenCV-Python Tutorials 참조
import cv2
import numpy as np

src1 = cv2.imread('./data/lena.jpg')
src2 = cv2.imread('./data/opencv_logo.png')
cv2.imshow('src2',  src2)

#1
rows,cols,channels = src2.shape
roi = src1[0:rows, 0:cols]  # src2의 전체 크기에 대한 src1의 영역을 roi에 저장.

#2
gray = cv2.cvtColor(src2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)    # 전경과 배경을 분할하기 위해 이진 영상 mask를 생성, 
mask_inv = cv2.bitwise_not(mask)    # 비트 반전 영상 mask_inv 생성.
cv2.imshow('mask',  mask)
cv2.imshow('mask_inv',  mask_inv)

#3
src1_bg = cv2.bitwise_and(roi, roi, mask = mask)    # roi 영상에서 mask의 255(흰색영역)인 화소에서만 bitwise_and() 함수로 src1의 배경 영역을 복사, 
cv2.imshow('src1_bg',  src1_bg)

#4
src2_fg = cv2.bitwise_and(src2, src2, mask = mask_inv)  # mask_inv 를 사용하여 src2에서 전경영역.
cv2.imshow('src2_fg',  src2_fg)

#5
##dst = cv2.add(src1_bg, src2_fg)   # 검은색 부분(0)과 or 연산하면 0 아닌 다른 값이 결과.
dst = cv2.bitwise_or(src1_bg, src2_fg)
cv2.imshow('dst',  dst)

#6
src1[0:rows, 0:cols] = dst  # Lena에 logo 크기만큼 dst 넣기.

cv2.imshow('result',src1)
cv2.waitKey(0)
cv2.destroyAllWindows()
