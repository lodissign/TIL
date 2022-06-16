# 0713.py
import cv2
import numpy as np
#1
def floodFillPostProcess(src, diff=(2,2,2)):    # cv2.floodFill() 함수를 이용하여 src를 복사한 img 영상에서 유사한 영역을 채워 분할한다.
    img = src.copy()
    rows, cols = img.shape[:2]
    mask   = np.zeros(shape=(rows+2, cols+2), dtype=np.uint8)
    for y in range(rows):
        for x in range(cols):
            if mask[y+1, x+1] == 0:
                r = np.random.randint(256)
                g = np.random.randint(256)
                b = np.random.randint(256)
                cv2.floodFill(img,mask,(x,y),(b,g,r),diff,diff)
    return img
#2
src = cv2.imread('./data/flower.jpg')
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
dst  = floodFillPostProcess(src)
dst2 = floodFillPostProcess(hsv)
cv2.imshow('src',src)
cv2.imshow('hsv',hsv)
cv2.imshow('dst',dst)
cv2.imshow('dst2',dst2)
#3
res = cv2.pyrMeanShiftFiltering(src, sp=5, sr=20, maxLevel=4)   # 평균 이동 필터링하여 res에 저장.
dst3 = floodFillPostProcess(res)

#4
term_crit=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 10, 2)
res2=cv2.pyrMeanShiftFiltering(hsv,sp=5,sr=20,maxLevel=4, termcrit=term_crit)
dst4 = floodFillPostProcess(res2)

cv2.imshow('res',res)
cv2.imshow('res2',res2)
cv2.imshow('dst3',dst3)
cv2.imshow('dst4',dst4)
cv2.waitKey()
cv2.destroyAllWindows()
