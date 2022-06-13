# 0401.py
import cv2
import numpy as np

img = cv2.imread('./data/lena.jpg') # cv2.IMREAD_COLOR. 'lena.jpg' 영상을 컬러 cv2.IMREAD_COLOR 영상으로 img에 읽는다. 
##img = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

print('img.ndim=', img.ndim)    # img 영상은 img.ndim=3 으로 3차원 배열이고,
print('img.shape=', img.shape)  # img.shape=(512,512,3)으로 512X512 크기의 3채널 영상이다. img.shape[0]은 영상의 세로 화소 크기 height, 1: 가로 화소 크기 width, 2: 채널 개수이다.
print('img.dtype=', img.dtype)  # 각 화소의 자료형은 img.dtype= uint8 로 부호 없는 8비트 정수이다.
# cv2.IMREAD_GRAYSCALE 영상으로 img에 읽으면 img.ndim=2, img.shape=(512,512), img.dtype=uint8.

img=img.astype(np.int32)    # img의 화소 자료형을 정수형으로 변경. 주요 화소 자료형은 np.bool, uint8, np.uint16, np.uint32, np.float32, np.float64, np.complex64 등이 있다.

print('img.dtype=',img.dtype)

img=np.uint8(img)   # img의 화소 자료형을 uint8로 변경 가능.
print('img.dtype=',img.dtype)

# 영상을 표시하기 위한 cv2.imshow() 함수는 uint8 자료형의 영상만을 화면에 표시한다.
