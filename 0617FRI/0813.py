# 0813.py
import cv2
import numpy as np

#1
src = cv2.imread('./data/banana.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, bImage = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)
##bImage = cv2.erode(bImage, None)
bImage = cv2.dilate(bImage, None)
##cv2.imshow('src',  src)
##cv2.imshow('bImage',  bImage)

mode   = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE
temp, contours, hierarchy = cv2.findContours(bImage, mode, method)

dst = src.copy()
##cv2.drawContours(dst, contours, -1, (255,0,0), 3)
cnt = contours[0]
cv2.drawContours(dst, [cnt], 0, (255,0,0), 3)

#2
dst2 = dst.copy()
rows,cols = dst2.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)  # cnt를 직선 [vx, vy, x, y]로 근사.
y1 =  int((-x*vy/vx) + y)
y2 = int(((cols-x)*vy/vx)+y)
cv2.line(dst2,(0,y1), (cols-1,y2),(0,0,255), 2)
cv2.imshow('dst2',  dst2)

#3
ellipse = cv2.fitEllipse(cnt)   # cnt를 타원 ellipse로 근사.
dst3 = dst.copy()
cv2.ellipse(dst3, ellipse,(0,0,255),2)
cv2.imshow('dst3',  dst3)

#4
poly = cv2.approxPolyDP(cnt, epsilon=20, closed=True)   # cnt를 다각형 poly로 근사.
dst4 = dst.copy()
cv2.drawContours(dst4, [poly], 0, (0,0,255), 2)
cv2.imshow('dst4',  dst4)

#5
dst5 = dst.copy()
for y in range(rows):
    for x in range(cols):
        if cv2.pointPolygonTest(cnt, (x, y), False)>0:  # (x,y)가 cnt의 내부의 점일 때,
            dst5[y, x] = (0, 255, 0)                    # dst5[y,x]를 초록색으로 변경-> 바나나의 내부 화소가 변경.
cv2.imshow('dst5',  dst5)

cv2.waitKey()
cv2.destroyAllWindows()
