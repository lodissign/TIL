# 0414.py
import cv2
import numpy as np
src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

dst = cv2.resize(src, dsize=(320, 240)) # cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation ]]]])-> dst. src는 입력 영상, dsize: 출력 영상의 크기, dst는 출력 영상, fx,fy: 가로, 세로 스케일, interpolation: cv2.INTER_NEAREST, cv2.INTER_LINEAR 디폴트, cv2.INTER_AREA, cv2.INTER_CUBIC, cv2.INTER_LANCZOS4 등의 보간법. 출력 영상 dst를 반환한다.
dst2 = cv2.resize(src, dsize=(0,0), fx=1.5, fy=1.2) # src를 가로 fx=1.5배, 세로 fy=1.2배로 변환하여 dst2에 저장. dst2.shape은 (614,768).

cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()    
cv2.destroyAllWindows()
