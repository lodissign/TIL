# 0603.py
import cv2
import numpy as np

#src = cv2.imread('./data/rect.jpg', cv2.IMREAD_GRAYSCALE)
src   = np.array([[0, 0, 1, 0],
                  [0, 0, 1, 0],
                  [0, 0, 1, 0],
                  [0, 0, 1, 0]], dtype=np.uint8)
src_1 = np.array([[0, 0, 1, 0],
                  [0, 0, 1, 0],
                  [1, 1, 1, 1],
                  [0, 0, 1, 0]], dtype=np.uint8)
src_2 = np.array([[1, 1, 2, 1],
                  [1, 1, 2, 1],
                  [2, 2, 2, 2],
                  [1, 1, 2, 1]], dtype=np.uint8)
src_3 = np.array([[0, 0, 0, 0, 0],
                  [0, 1, 1, 1, 0],
                  [0, 1, 1, 1, 0],
                  [0, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0]], dtype=np.uint8)                  

#1
gx = cv2.Sobel(src, cv2.CV_32F, 1, 0, ksize = 3)
gy = cv2.Sobel(src, cv2.CV_32F, 0, 1, ksize = 3)
print('gx:\n', gx)
print('gy:\n', gy)

#2
dstX = cv2.sqrt(np.abs(gx))
print('dstX_1:\n', dstX)
dstX = cv2.normalize(dstX, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
print('dstX_2:\n', dstX)

#3
dstY = cv2.sqrt(np.abs(gy))
dstY = cv2.normalize(dstY, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

#4
mag   = cv2.magnitude(gx, gy)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(mag)
#print('mag:', minVal, maxVal, minLoc, maxLoc)
print('mag:\n', mag)

dstM = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# cv2.imshow('src',  src)
# cv2.imshow('dstX',  dstX)    
# cv2.imshow('dstY',  dstY)
# cv2.imshow('dstM',  dstM)

print('src:\n', src)
print('dstX:\n', dstX)
print('dstY:\n', dstY)
print('dstM:\n', dstM)



cv2.waitKey()
cv2.destroyAllWindows()
