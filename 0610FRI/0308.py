#0308.py
import cv2
import numpy as np

img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255

pts1 = np.array([[100, 100], [200, 100], [200, 200], [100, 200]])
pts2 = np.array([[300, 200], [400, 100], [400, 200]])

cv2.fillConvexPoly(img, pts1, color=(255, 0, 0))    # 볼록다각형 pts1을 파란색으로 채운다.

# cv2.fillPoly(img, [pts2], color=(0, 0, 255))        # 다각형 pts2의 배열 [pts2]를 빨간색으로 채운다.
cv2.fillPoly(img, [pts1, pts2], color=(0, 0, 255))  # pts1, pts2를 리스트[]로 감싸지 않으면 오류 발생.

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
