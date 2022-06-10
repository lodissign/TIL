#0301.py
import cv2
import numpy as np

# img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255 # np.zeros()는 영상으로 사용할 0으로 초기화된 배열 numpy.ndarry을 생성한다. shape=(512,512,3)은 512X512 크기의 3채널 컬러 영상, dtype=np.uint8은 영상 화소가 부호 없는 8비트 정수이다. 화소값이 (0,0,0)이면 검은색 배경 영상.

# img = np.ones((512,512,3), np.uint8) * 255
# img = np.full((512,512,3), (255, 255, 255), dtype= np.uint8)
img = np.zeros((512,512, 3), np.uint8) # Black 배경

pt1 = 100, 100
pt2 = 400, 400
cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)    # cv2.rectangle()로 img 영상에 pt1(100,100), pt2(400,400)에 의해서 정의되는 사각형을 녹색(0,255,0), 두께 2로 그린다.

cv2.line(img, (0, 0), (500, 0), (255, 0, 0), 5) # cv2.line()으로 img 영상에 원점 (0,0)에서 좌표 (500,0)로 파란색(255,0,0), 두께 5로 그린다.
cv2.line(img, (0, 0), (0, 500), (0,0,255), 5)   # 빨간색 선.

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
