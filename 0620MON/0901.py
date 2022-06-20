# 0901.py
import cv2
import numpy as np
 
src = cv2.imread('./data/chessBoard.jpg')
gray= cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

#1
##fastF = cv2.FastFeatureDetector_create()
##fastF =cv2.FastFeatureDetector.create()
fastF =cv2.FastFeatureDetector.create(threshold=30) # 특징 검출기 fastF 객체 생성.
kp = fastF.detect(gray)     # 특징점 검출.
dst = cv2.drawKeypoints(gray, kp, None, color=(0,0,255))    # 특징점 그리기.
print('len(kp)=', len(kp))
cv2.imshow('dst',  dst)

#2
fastF.setNonmaxSuppression(False)   # 지역 극값 억제 하지 않고 특징점 검출하면 갯수가 늘어난다.
kp2 = fastF.detect(gray)
dst2 = cv2.drawKeypoints(src, kp2, None, color=(0,0,255))
print('len(kp2)=', len(kp2))
cv2.imshow('dst2',  dst2)

#3
dst3 = src.copy()
points = cv2.KeyPoint_convert(kp)   # 특징점 kp를 좌표 리스트 points에 반환.
points = np.int32(points)

for cx, cy in points:
    cv2.circle(dst3, (cx, cy), 3, color=(255, 0, 0), thickness=1)
cv2.imshow('dst3',  dst3)
cv2.waitKey()
cv2.destroyAllWindows()
