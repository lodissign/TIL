# 0706.py
import cv2
import numpy as np

#1
src = np.zeros(shape=(512,512,3), dtype=np.uint8)
cv2.rectangle(src, (50, 100), (450, 400), (255, 255, 255), -1)
cv2.rectangle(src, (100, 150), (400, 350), (0, 0, 0), -1)
cv2.rectangle(src, (200, 200), (300, 300), (255, 255, 255), -1)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

#2
mode = cv2.RETR_EXTERNAL    # 리스트 contours에 len(contours)=1개의 가장 외곽의 윤곽선 검출.
method = cv2.CHAIN_APPROX_SIMPLE    # 윤곽선을 다각형으로 근사한 좌표를 반환.
##method =cv2.CHAIN_APPROX_NONE # 이 경우 contours[0].shape가 (1400,1,2)로 윤곽선 위의 모든 좌표 1400개 검출.
temp, contours, hierarchy = cv2.findContours(gray, mode, method)  # mode, method 사용하여 윤곽선 검출. contours[0].shape=(4,1,2)로 4개의 검출된 좌표가 (1,2) 배열에 저장.

print('type(contours)=', type(contours))
print('type(contours[0])=', type(contours[0]))
print('len(contours)=', len(contours))
print('contours[0].shape=', contours[0].shape)
print('contours[0]=', contours[0])

#3
cv2.drawContours(src, contours, -1, (255,0,0), 3)   # 검출된 윤곽선 contours를 모두 src에 파란색 두께 3으로 그린다.

#4
for pt in contours[0][:]: 
    cv2.circle(src, (pt[0][0], pt[0][1]), 5, (0,0,255), -1) # 중심점 (pt[0][0], pt[0][1]), 반지름 5, 빨간색으로 채워진 원을 src에 그린다.

cv2.imshow('src',  src)
cv2.waitKey()
cv2.destroyAllWindows()
