# 0205.py
import cv2
from   matplotlib import pyplot as plt

imageFile = './data/lena.jpg'
imgGray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)

plt.figure(figsize=(6,6))   # 크기를 (6인치, 6인치)로 설정.
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)   # 영상 출력 범위를 좌우[0,1], 위아래[0,1]로 조정. 범위는 left<right, bottom<top 이어야 함.
plt.imshow(imgGray, cmap = 'gray')  # imgGray 영상을 스케이스케일로 화면에 표시.

plt.axis('off')
plt.savefig('./data/0205.png')  # 영상을 '0205.png' 파일에 저장.
plt.show()
