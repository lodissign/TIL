# 0503.py
import cv2
import numpy as np

src = np.array([[0, 0, 0, 0],
              [1, 1, 3, 5],
              [6, 1, 1, 3],
              [4, 3, 1, 7]
              ], dtype=np.uint8)

hist1 = cv2.calcHist(images=[src], channels=[0], mask=None,
                    histSize=[4], ranges=[0, 8])    # 4x4 배열 src의 0번 채널에서 mask 지정 없이, 히스토그램 bin 갯수 4, 범위 [0,8](0은 포함, 8은 포함X) 로 히스토그램 hist1 계산. 단일 bin range = range / hist size. 8/4=2. 0,1: 9개, 2,3: 3개, 4,5: 2개, 6,7: 2개.
print('hist1 = ', hist1)

hist2 = cv2.calcHist(images=[src], channels=[0], mask=None,
                    histSize=[4], ranges=[0, 4])    # 
print('hist2 = ', hist2)
