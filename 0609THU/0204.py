# 0204.py
import cv2
from   matplotlib import pyplot as plt

imageFile = './data/lena.jpg'
imgGray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)   # 그레이스케일로 영상을 읽어 imgGray에 할당. 컬러 영상으로 읽어 cvtColor() 함수를 이용하여 그케이스케일 영상으로 변경할 수도 있다.
plt.axis('off')

plt.imshow(imgGray, cmap = "gray", interpolation='bicubic') # imgGray 영상을 gray 컬러맵(cmap), bicubic으로 보간(interpolation. 알려진 값 사이(중간)에 위치한 값을 알려진 값으로부터 추정)
plt.show()
