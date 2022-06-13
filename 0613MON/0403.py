# 0403.py
import cv2
##import numpy as np

img = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
img[100, 200] = 0  # img 영상의 y=100(행), x=200(열) 화소의 값(밝기, 그레이스케일)을 0으로 변경. img[100,200]은 img[100][200]과 같다. 화소의 인덱스는 y(행), x(열) 순으로 지정.
print(img[100:110, 200:210])    # numpy의 슬라이싱으로 y=100에서 y=109까지, x=200에서 x=209까지의 10X10 사각 영역을 ROI로 지정하여 화소값을 출력.

##for y in range(100, 400):
##    for x in range(200, 300):
##        img[y, x] = 0

img[100:400, 200:300] = 0 

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
