# 0513.py
# BGR 컬러 영상 src를 BGR 컬러 영상의 히스토그램 평활화는 HSV, YCrCb 등의 컬러 모델로 변환한 다음,
# 밝기값 컬러 채널 (V,Y)에 히스토그램 평활화를 적용하고 BGR 컬러 영상으로 변환.
import cv2
import numpy as np

src = cv2.imread('./data/lena.jpg')
cv2.imshow('src',  src)

#1
hsv    = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)   # BGR 컬러 영상 src를 HSV 컬러 영상 hsv로 변환하고,
h, s, v = cv2.split(hsv)    # cv2.split() 함수로 hsv를 h,s,v에 채널 분리한다.

v2 = cv2.equalizeHist(v)    # v를 v2에 히스토그램 평활화.
hsv2 = cv2.merge([h, s, v2])    # [h,s,v2]를 hsv2에 채널 합성.
dst    = cv2.cvtColor(hsv2, cv2.COLOR_HSV2BGR)  # HSV 컬러 영상 hsv2를 BGR 컬러 영상으로 dst에 변환.
cv2.imshow('dst',  dst) # 원본 영상에 비해 선명한 느낌.

#2
yCrCv = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
y, Cr, Cv = cv2.split(yCrCv)

y2 = cv2.equalizeHist(y)
yCrCv2 = cv2.merge([y2, Cr, Cv])
dst2    = cv2.cvtColor(yCrCv2, cv2.COLOR_YCrCb2BGR)

cv2.imshow('dst2',  dst2)   # dst 만큼 진하지는 않지만 원본 영상에 비해 선명한 느낌.
cv2.waitKey()    
cv2.destroyAllWindows()
