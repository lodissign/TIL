# 0504.py
import cv2
import numpy as np
from   matplotlib import pyplot as plt

src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

hist1 = cv2.calcHist(images=[src], channels=[0], mask=None,
                    histSize=[32], ranges=[0, 256]) 

hist2 = cv2.calcHist(images=[src], channels=[0], mask=None,
                    histSize=[256], ranges=[0, 256])
#1
hist1 = hist1.flatten() # hist1.shape=(32, )인 1차원 행 배열.
hist2 = hist2.flatten()

#2
plt.title('hist1: binX = np.arange(32)')
plt.plot(hist1, color='r')  # 꺾은 선 그래프.
binX = np.arange(32)    # 가로축은 빈의 인덱스.

plt.bar(binX, hist1, width=1, color='b')    # 막대 그래프.
plt.show()

#3
plt.title('hist1: binX = np.arange(32)*8')
binX = np.arange(32)*8  # 빈의 x축 넓이만 *8 한 거라 그래프 모양은 그대로.
plt.plot(binX, hist1, color='r')
plt.bar(binX, hist1, width=8, color='b')
plt.show()

#4
plt.title('hist2: binX = np.arange(256)')
plt.plot(hist2, color='r')
binX = np.arange(256)   # 빈의 갯수가 늘어나서 각각 하나의 값을 가지므로 더 촘촘한 모양.
plt.bar(binX, hist2, width=1, color='b')
plt.show()
