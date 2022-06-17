# 0807.py
import cv2
import numpy as np

#1
src = cv2.imread('./data/chessBoard.jpg')   # 체스보스 패턴의 내부 코너점은 6x3이다.
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
patternSize = (6, 3)
found, corners = cv2.findChessboardCorners(src, patternSize)    # (6,3) 패턴 크기의 코너점을 corners에 검출.
print('corners.shape=', corners.shape)

#2
term_crit=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 10, 0.01)
corners2 = cv2.cornerSubPix(gray, corners, (5,5), (-1,-1), term_crit)

#3
dst = src.copy()
cv2.drawChessboardCorners(dst, patternSize, corners2, found)

cv2.imshow('dst',  dst) 
cv2.waitKey()
cv2.destroyAllWindows()
