# 0410.py
import cv2
import numpy as np
 
src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
shape = src.shape[0], src.shape[1], 3
dst = np.zeros(shape, dtype=np.uint8)   # src 와 같은 가로, 세로 크기의 3-채널 컬러 영상 dst 생성.

dst[:,:,0] = src  # dst의 0-채널 blue에 src 를 얕은 복사.
##dst[:,:,1] = src 
##dst[:,:,2] = src

dst[100:400, 200:300, :] = [255, 255, 255]  # dst만 해당 영역 흰색으로 변경 됨.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()    
cv2.destroyAllWindows()
