# 0811.py
import cv2
import numpy as np

#1
src = cv2.imread('./data/momentTest.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, bImage = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

mode = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE
temp, contours, hierarchy = cv2.findContours(bImage, mode, method)

dst = src.copy()
cnt = contours[0]
cv2.drawContours(dst, [cnt], 0, (255,0,0), 3)

#2
M = cv2.moments(cnt)
hu = cv2.HuMoments(M)
print('hu.shape=', hu.shape)
print('hu=', hu)

#3
angle = 45.0
scale = 0.2
cx = M['m10']/M['m00']
cy = M['m01']/M['m00']
center = (cx, cy)
t = (20, 30)
A = cv2.getRotationMatrix2D( center, angle, scale ) # center를 중심으로 45도 회전, 0.2 축소하는 2x3 어파인 변환 행렬 A 계산.
A[:, 2] += t    # t만큼의 이동 반영.
print('A=', A)

cnt2 = cv2.transform(cnt, A)    # cnt에 어파인 행렬 A를 적용하여 변한 윤곽선 cnt2 생성.
cv2.drawContours(dst, [cnt2], 0, (0,255,0), 3)  # dst에 초록색으로 그림.
cv2.imshow('dst',  dst)

#4
M2 = cv2.moments(cnt2)
hu2 = cv2.HuMoments(M2)
print('hu2.shape=', hu2.shape)
print('hu2=', hu)

#5
##diffSum = sum(abs(hu - hu2))
diffSum = np.sum(cv2.absdiff(hu, hu2))  # hu, hu2가 정확히 같지 않은 이유는 영상의 해상도 문제.
print('diffSum=', diffSum)

cv2.waitKey()
cv2.destroyAllWindows()
