# 0201.py
import cv2  # 파이썬에서 OpenCV를 사용하기 위해 cv2를 import. OpenCV 함수는 cv2를 이용하여 접근.
import numpy as np

imageFile = './data/lena.jpg'
img  = cv2.imread(imageFile)    # cv2.IMREAD_COLOR. imageFile 파일을 cv2.imread() 함수를 이용하여 컬러 영상으로 img에 읽는다. cv2.imread(imageFile, cv2.IMREAD_COLOR)와 같다. img의 자료형은 'numpy.ndarray'이고, img.shape은 (512, 512, 3)으로 512X512 크기의 3채널 컬러 영상이다. 영상의 채널 순서는 BGR 순서이다.
img2 = cv2.imread(imageFile, 0) # cv2.IMREAD_GRAYSCALE. 그레이스케일 영상으로 img2에 읽는다. img2.shape은 (512, 512)로 1채널 그레이스케일 영상이다.

##encode_img = np.fromfile(imageFile, np.uint8)
##img = cv2.imdecode(encode_img, cv2.IMREAD_UNCHANGED)

cv2.imshow('Lena color',img)    # cv2.imshow() 함수를 이용하여 img 영상을 윈도우 'Lena color'에 표시.
cv2.imshow('Lena grayscale',img2)

cv2.waitKey()   # delay=0으로 키보드 입력이 있을 때까지 무한 대기시켜, 윈도우를 계속 화면에 표시한다. 
cv2.destroyAllWindows() # 윈도우가 포커스 받은 상태에서 키보드 임의의 키를 누르면 cv2.destroyAllWindows() 함수로 윈도우를 파괴(닫음)

