# 0417.py
import cv2
import numpy as np

src1 = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
src2 = np.zeros(shape=(512,512), dtype=np.uint8) + 100

dst1 = src1 + src2  # numpy의 배열 덧셈으로 255가 넘는 경우 256으로 나눈 나머지가 저장.
dst2 = cv2.add(src1, src2)  # 255를 넘는 경우 255로 저장.
dst3 = cv2.add(src1, src2, dtype = cv2.CV_8U)  # 화소 자료형 dtype을 cv2.CV_8U (8비트 unsigned 정수)와 같이 명시 가능.

cv2.imshow('dst1',  dst1)
cv2.imshow('dst2',  dst2)
cv2.imshow('dst3',  dst3)
cv2.waitKey()    
cv2.destroyAllWindows()
