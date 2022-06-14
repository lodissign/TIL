# 0514.py
import cv2
import numpy as np

src = np.array([[2, 2, 2, 2, 0,   0,   0,   0],
                [2, 1, 1, 2, 0,   0,   0,   0],
                [2, 1, 1, 2, 0,   0,   0,   0],
                [2, 2, 2, 2, 0,   0,   0,   0],
                [0, 0, 0, 0, 255, 255, 255, 255],
                [0, 0, 0, 0, 255, 1,   1,   255],
                [0, 0, 0, 0, 255, 1,   1,   255],
                [0, 0, 0, 0, 255, 255, 255, 255]], dtype=np.uint8)

#1
clahe = cv2.createCLAHE(clipLimit=40, tileGridSize=(1,1))   # clipLimit=40, tileGridSize=(1,1)로 clahe 객체 생성,
dst = clahe.apply(src)  # dst에 평활화.
# tileGridSize=(1,1), tileArea=8*8이다. 
# 8-비트 그레이트스케일 영상에서 histSize=256이므로 clipLimit= 40*64/256=10이다.
# tileGridSize=(1,1) 이므로 히스토그램은 1개만 계산.
# 히스토그램에서 clipLimit=10 보다 큰 값은 히스토그램에 균등하게 재분배한다.
print("dst=\n", dst)

#2
clahe2 = cv2.createCLAHE(clipLimit=40, tileGridSize=(2,2))
dst2 = clahe2.apply(src)
print("dst2=\n", dst2)
