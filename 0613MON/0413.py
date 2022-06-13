# 0413.py
import cv2
src = cv2.imread('./data/lena.jpg')

gray   = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # BGR 채널 컬러 영상 src를 GRAY 영상 gray로 변환.
yCrCv = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
hsv    = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

cv2.imshow('gray',  gray)
cv2.imshow('yCrCv', yCrCv)
cv2.imshow('hsv',   hsv)

cv2.waitKey()    
cv2.destroyAllWindows()
