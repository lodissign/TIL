# 0501.py
import cv2
import numpy as np
src = cv2.imread('./data/heart10.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('src',  src)

ret, dst = cv2.threshold(src, 120, 255, cv2.THRESH_BINARY)  # thresh=120, max_val=255, type=cv2.THRESH_BINARY로 임계값을 적용하여 이진 영상 dst 생성(120보다 크면 255, 작거나 같으면 0). ret=120.
print('ret=', ret)
cv2.imshow('dst',  dst)

ret2, dst2 = cv2.threshold(src, 200, 255,
                             cv2.THRESH_BINARY+cv2.THRESH_OTSU) # 임계값 200은 무시하고 Otsu 알고리즘으로 최적의 임계값을 찾아내서 ret2=175로 계산.
print('ret2=', ret2)
cv2.imshow('dst2',  dst2)

cv2.waitKey()    
cv2.destroyAllWindows()
