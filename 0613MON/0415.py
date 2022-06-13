# 0415.py
import cv2
src = cv2.imread('./data/lena.jpg')

dst1 = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE) # 시계 방향으로 90도 회전.
dst2 = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
# rotateCode는 cv2.ROTATE_90_CLOCKWISE, cv2.ROTATE_180, cv2.ROTATE_90_COUNTERCLOCKWISE 등이 있다.

cv2.imshow('dst1',  dst1)
cv2.imshow('dst2',  dst2)
cv2.waitKey()    
cv2.destroyAllWindows()
