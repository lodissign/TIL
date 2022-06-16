# 0701.py
import cv2
import numpy as np

src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

edges1 = cv2.Canny(src, 50, 100)    # threshold1=50, threshold2=100, aperturSize=3(그래디언트를 계산하기 위한 Sobel 필터의 크기). 
# 높은 값의 임계값(threshold2) 이상은 강한 에지로 확신하고, 미만부터 낮은 값의 임계값(threshold1)까지는 약한 에지로 판단하여 추가적인 검사.
# 히스테리시스 임계값(hysteresis thresholding)으로 강한 에지와 연결된 약한 에지는 에지로 판단.
# Sobel 에지보다 가늘어 짐.
edges2 = cv2.Canny(src, 50, 200)    # edges1보다 적은 에지가 검출.
 
cv2.imshow('edges1',  edges1)
cv2.imshow('edges2',  edges2)
cv2.waitKey()
cv2.destroyAllWindows()
