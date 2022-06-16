# 0704.py
import cv2
import numpy as np

#1
src1 = cv2.imread('./data/circles.jpg')
gray1 = cv2.cvtColor(src1,cv2.COLOR_BGR2GRAY)
circles1 = cv2.HoughCircles(gray1, method = cv2.HOUGH_GRADIENT,
            dp=1, minDist=50, param2=15)    # param2는 원 검출을 위한 어큐뮬레이터의 임계값으로 원 위의 에지 갯수이다. 검출된 원의 중심 cx, cy, 반지름 r을 저장한 circles1 배열은 circles.shape=(1,3,3)으로 circles[0]의 3개의 행에 원의 cx, ,y, r을 저장.

circles1 =  np.int32(circles1)
print('circles1.shape=', circles1.shape)
for circle in circles1[0,:]:    
    cx, cy, r  = circle
    cv2.circle(src1, (cx, cy), r, (0,0,255), 2)
cv2.imshow('src1',  src1)

#2
src2 = cv2.imread('./data/circles2.jpg')
gray2 = cv2.cvtColor(src2,cv2.COLOR_BGR2GRAY)
circles2 = cv2.HoughCircles(gray2, method = cv2.HOUGH_GRADIENT,
          dp=1, minDist=50, param2=15, minRadius=30, maxRadius=100) # 원의 반지름 범위를 30~100 으로 제한하여 원을 검출. circles1 배열은 circles.shape=(1,6,3)으로 6개의 행에 원의 cx, cy, r을 저장.

circles2 =  np.int32(circles2)
print('circles2.shape=', circles2.shape)
for circle in circles2[0,:]:    
    cx, cy, r  = circle
    cv2.circle(src2, (cx, cy), r, (0,0,255), 2) 
cv2.imshow('src2',  src2)
cv2.waitKey()
cv2.destroyAllWindows()
