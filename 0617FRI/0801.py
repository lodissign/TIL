# 0801.py
import cv2
import numpy as np
#1
def findLocalMaxima(src):   # src에서 팽창과 침식의 모폴로지 연산으로 지역 극대값의 좌표를 points 배열에 검출하여 반환.
    kernel= cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(11,11))
    dilate = cv2.dilate(src,kernel) 
    localMax = (src == dilate)
    
    erode = cv2.erode(src,kernel)
    localMax2 = src > erode      
    localMax &= localMax2
    points = np.argwhere(localMax == True)
    points[:,[0, 1]] = points[:,[1, 0]] 
    return points

#2
src = cv2.imread('./data/CornerTest.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
res = cv2.preCornerDetect(gray, ksize=3)
ret, res2 = cv2.threshold(np.abs(res), 0.1, 0, cv2.THRESH_TOZERO)   # 극대값만을 찾기 위하여 np.abs(res)인 절대값 배열에서 0.1 보다 작은 값은 0으로 변경하여 res2에 저장.
corners = findLocalMaxima(res2)
print('corners.shape=', corners.shape)

#3
dst = src.copy()  
for x, y in corners:    
    cv2.circle(dst, (x, y), 5, (0,0,255), 2)
    
cv2.imshow('dst',  dst) 
cv2.waitKey()
cv2.destroyAllWindows()
