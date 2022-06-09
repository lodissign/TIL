# 0203.py
import cv2
from   matplotlib import pyplot as plt  # matplotlib 패키지에서 pyplot을 plt 이름으로 import.

imageFile = './data/lena.jpg'
imgBGR = cv2.imread(imageFile)
plt.axis('off') # x,y 축을 표시하지 않음.

imgRGB = cv2.cvtColor(imgBGR,cv2.COLOR_BGR2RGB) # OpenCV로 읽은 컬러 영상 imgBGR을 cvtColor()로 RGB 채널 순서로 변경. OpenCV는 컬러 영상을 BGR 채널 순서로 처리하고, Matplotlib 는 RGB 채널 순서로 처리하기 때문.
# plt.imshow(imgRGB)  # imgRGB를 출력.
plt.imshow(imgBGR)  # imgBGR를 출력.
plt.show()  # 윈도우에 표시. 
