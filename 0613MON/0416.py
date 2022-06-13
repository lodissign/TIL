# 0416.py
import cv2
src = cv2.imread('./data/lena.jpg')

rows, cols, channels = src.shape
M1 = cv2.getRotationMatrix2D( (rows/2, cols/2),  45, 0.5 )  # 영상의 중심인 center = (rows/2, cols/2)를 기준으로 scale=0.5로 축소, angle=45도 (반시계방향) 으로 회전한 어파인 변환행렬 M1을 생성. 
M2 = cv2.getRotationMatrix2D( (rows/2, cols/2), -45, 1.0 )  # -45도 (시계방향).

dst1 = cv2.warpAffine( src, M1, (rows, cols))   # src 영상에 2x3 어파인 변환행렬 M1을 적용하여 (rows, cols)크기의 dst1 영상을 생성.
dst2 = cv2.warpAffine( src, M2, (rows, cols))

cv2.imshow('dst1',  dst1)
cv2.imshow('dst2',  dst2)
cv2.waitKey()    
cv2.destroyAllWindows()
