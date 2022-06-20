# 0905.py
import cv2
import numpy as np
 
src = cv2.imread('./data/chessBoard.jpg')
gray= cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

#1
##goodF = cv2.GFTTDetector.create()
goodF = cv2.GFTTDetector_create()
kp= goodF.detect(gray)
print('len(kp)=', len(kp))
dst = cv2.drawKeypoints(gray, kp, None, color=(0,0,255))   
cv2.imshow('dst',  dst)

#2
goodF2 = cv2.GFTTDetector_create(maxCorners= 50,    # 최대 코너점 개수
                                qualityLevel=0.1,   # cv2.cornerHarris() 또는 cv2.cornerMinEigenVal()로 계산한 코너점 측정값 중에서 최대값 maxQuality에 곱해져, 코너점 측정값이 qualityLevel * maxQuality보다 작은 모든 코너점을 제거한다.
                                minDistance = 10,   # 코너점 사이의 최소거리.
                                useHarrisDetector=True) # True: cv2.cornerHarris()로 코너점 계산, False: cv2.cornerMinEigenVal() 사용.
kp2= goodF2.detect(gray)
print('len(kp2)=', len(kp2))
dst2 = cv2.drawKeypoints(gray, kp2, None, color=(0,0,255))   
cv2.imshow('dst2',  dst2)
cv2.waitKey()
cv2.destroyAllWindows()
