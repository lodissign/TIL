# 0712.py
import cv2
import numpy as np
#1
src = cv2.imread('./data/lena.jpg')

down2 = cv2.pyrDown(src)    # src를 가로 세로 각각 1/2배로 축소한 피라미드 영상. 
down4 = cv2.pyrDown(down2)  # down2를 가로 세로 각각 1/2배로 축소한 피라미드 영상. 
print('down2.shape=', down2.shape)  # down2.shape=(256,256,3).
print('down2.shape=', down2.shape)  # shape 동일.

#2
up2 = cv2.pyrUp(src)    # 가로 세로 각각 2배.
up4 = cv2.pyrUp(up2)
print('up2.shape=', up2.shape)  # up2.shape=(1024, 1024, 3).
print('up4.shape=', up4.shape)  # up4.shape=(2048, 2048, 3).

cv2.imshow('down2',down2)
##cv2.imshow('down4',down4)
cv2.imshow('up2',up2)
##cv2.imshow('up4',up4)
cv2.waitKey()
cv2.destroyAllWindows()
