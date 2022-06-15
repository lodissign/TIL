# 0606.py
import cv2
import numpy as np

#1
#src  = cv2.imread('./data/A.bmp', cv2.IMREAD_GRAYSCALE)
src  = cv2.imread('./data/rect.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('src',src)
#src  = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
blur = cv2.GaussianBlur(src, ksize=(7, 7), sigmaX=0.0)  # 입력 영상 src를 부드럽게 하여 미분 오차를 줄이기 위해 ksize=(7,7)의 가우시안 블러링.
lap = cv2.Laplacian(blur, cv2.CV_32F,3) # 라플라시안 필터링.

##ret, edge = cv2.threshold(np.abs(lap), 10, 255, cv2.THRESH_BINARY)
##edge = edge.astype(np.uint8)
##cv2.imshow('edge',  edge)

#2
def SGN(x):
    if x >= 0:
        sign = 1
    else:
        sign = -1
    return sign

def zeroCrossing(lap):  # 영교차 검출.
    height, width = lap.shape
    Z = np.zeros(lap.shape, dtype=np.uint8)    
    for y in range(1, height-1):
        for x in range(1,width-1):
            neighbors=[lap[y-1,x], lap[y+1,x], lap[y,x-1], lap[y,x+1],
                       lap[y-1,x-1], lap[y-1,x+1], lap[y+1,x-1], lap[y+1,x+1]]  # 8개의 이웃 중에 마주 보는 화소 4쌍.          
            mValue= min(neighbors)  # 4쌍 중 제일 작은 값.
            if SGN(lap[y,x]) != SGN(mValue):    # 부호가 다른 쌍은 영-교차점으로 판단.
                Z[y, x] = 255
    return Z
edgeZ = zeroCrossing(lap)
cv2.imshow('Zero Crossing',  edgeZ)
cv2.waitKey()    
cv2.destroyAllWindows()
