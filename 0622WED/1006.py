# 1006.py
import cv2
import numpy as np

#1
def drawFlow(img, flow, thresh=2, stride=8): # img영상에 광류 flow를 벡터로 표시.
     h, w = img.shape[:2]
     mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])   # flow부터 벡터의 크기 mag와 각도 ang를 계산. 각도 ang는 라디안 [0,2]로 계산.
     flow2 = np.int32(flow)
     for y in range(0,h,stride):   # 광류 flow가 모든 화소에서 계산하기 때문에, 벡터로 표현하기 위하여 stride 간격에서 벡터 크기가 thresh보다 큰 벡터만을 표시.
          for x in range(0,w,stride):
               dx, dy = flow2[y,x]
               if mag[y,x] > thresh:
                    cv2.circle(img, (x, y), 2, (0,255,0), -1)
                    cv2.line(img, (x, y), (x+dx, y+dy),(255, 0, 0), 1)
#2          
cap = cv2.VideoCapture('./data/vtest.avi')
if (not cap.isOpened()): 
     print('Error opening video')
     
height, width = (int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
                 int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))

hsv = np.zeros((height, width, 3), dtype=np.uint8)

ret, frame = cap.read()
imgP = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

TH = 2
AREA_TH = 50
mode = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE
params = dict(pyr_scale=0.5, levels=3, winsize=15,
              iterations=3, poly_n=5, poly_sigma=1.2, flags=0)   # 광류 검출을 위한 매개변수.
#3 
t = 0
while True:
     ret, frame = cap.read()
     if not ret: break
     t+=1
     print('t=',t)
     imgC = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     imgC = cv2.GaussianBlur(imgC, (5, 5), 0.5)
#3-1
     flow = cv2.calcOpticalFlowFarneback(imgP,imgC,None, **params)
     drawFlow(frame, flow, TH)

#3-2     
     mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])      # 광류 flow의 크기는 mag, 각도는 라디안으로 ang에 계산.
     ret, bImage = cv2.threshold(mag,TH,255,cv2.THRESH_BINARY)
     bImage = bImage.astype(np.uint8)
     contours, hierarchy = cv2.findContours(bImage, mode, method)
     for i, cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        if area > AREA_TH:
            x, y, width, height = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+width, y+height), (0,0,255), 2)
#3-3
     cv2.imshow('frame',frame)
     imgP = imgC.copy()
     key = cv2.waitKey(25)
     if key == 27:
          break
if cap.isOpened():
    cap.release();
cv2.destroyAllWindows()
