# 0419.py
import cv2
import numpy as np

src1 = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
src2 = np.zeros(shape=(512,512), dtype=np.uint8)+255    # 그레이스케일 하얀 배경.

dst1 = 255 - src1   # src1 의 반전 영상.
dst2 = cv2.subtract(src2, src1) # dst1 과 같은 값.
dst3 = cv2.compare(dst1, dst2, cv2.CMP_NE)  # dst1, dst2 가 같은 값이라 모두 0-> 검정. cv2.CMP_EQ, cv2.CMP_NE, cv2.CMP_GT, cv2.CMP_GE, cv2.CMP_LT, cv2.CMP_LE 등의 비교 가능.
n    = cv2.countNonZero(dst3)   # dst3 에서 0이 아닌 화소를 카운트하여 반환.
print('n = ', n)

cv2.imshow('dst1',  dst1)
cv2.imshow('dst2',  dst2)
cv2.imshow('dst3',  dst3)
cv2.imshow('n',  n)
cv2.waitKey()    
cv2.destroyAllWindows()
