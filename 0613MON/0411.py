# 0411.py
import cv2
src = cv2.imread('./data/lena.jpg')

dst = cv2.split(src)    # 3-채널 BGR 컬러 영상 src를 채널 분리하여 튜블 dst에 저장.
print(type(dst))
print(type(dst[0])) # type(dst[1]), type(dst[2])

cv2.imshow('blue',  dst[0])
cv2.imshow('green', dst[1])
cv2.imshow('red',   dst[2])
cv2.waitKey()    
cv2.destroyAllWindows()
