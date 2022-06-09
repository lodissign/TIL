# 0206.py
import cv2
from   matplotlib import pyplot as plt

path = './data/'
imgBGR1 = cv2.imread(path+'lena.jpg')
imgBGR2 = cv2.imread(path+'apple.jpg')
imgBGR3 = cv2.imread(path+'baboon.jpg')
imgBGR4 = cv2.imread(path+'orange.jpg')
# cv2.imread() 함수로 파일들을 읽는다.

imgRGB1 = cv2.cvtColor(imgBGR1, cv2.COLOR_BGR2RGB)
imgRGB2 = cv2.cvtColor(imgBGR2, cv2.COLOR_BGR2RGB)
imgRGB3 = cv2.cvtColor(imgBGR3, cv2.COLOR_BGR2RGB)
imgRGB4 = cv2.cvtColor(imgBGR4, cv2.COLOR_BGR2RGB)
# cvtColor() 함수로 BGR 채널에서 RGB 채널의 영상으로 변환.

fig, ax = plt.subplots(2, 2, figsize=(10,10), sharey=True)  # 2X2 subplot을 figsize=(10,10) 크기로 ax에 생성.
fig.canvas.manager.set_window_title('Sample Pictures')  # Figure 객체 fig를 이용하여 윈도우 타이틀을 'Sample Pictures'로 변경.

ax[0][0].axis('off')    # 좌표축 없앰.
ax[0][0].imshow(imgRGB1, aspect = 'auto')   # aspect = 'auto' 를 지우면 영상이 안 나옴.

ax[0][1].axis('off')
ax[0][1].imshow(imgRGB2, aspect = 'auto')

ax[1][0].axis("off")
ax[1][0].imshow(imgRGB3, aspect = "auto")

ax[1][1].axis("off")
ax[1][1].imshow(imgRGB4, aspect = 'auto')

plt.subplots_adjust(left=0, bottom=0, right=1, top=1,   # 그림 크기 설정.
                    wspace=0.05, hspace=0.05)       # 서브플롯 사이의 가로세로 여백.
plt.savefig("./data/0206.png", bbox_inches='tight')
plt.show()
