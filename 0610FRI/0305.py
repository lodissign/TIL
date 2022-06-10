#0305.py
import cv2
import numpy as np

img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255

pts1 = np.array([[100, 100], [200, 100], [200, 200], [100, 200]])   # 4개의 좌표를 갖는 다각형(사각형)을 pts1 배열 numpy.ndarray에 생성.
pts2 = np.array([[300, 200], [400, 100], [400, 200]])   # 3개의 좌표를 갖는 다각형(삼각형).

cv2.polylines(img, [pts1, pts2], isClosed=True, color=(255, 0, 0))  # [pts1, pts2]로 2개의 닫힌 다각형을 파란색으로 그린다.

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
