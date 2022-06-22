# 1005.py
import cv2
import numpy as np

#1
roi  = None
drag_start = None
mouse_status = 0
tracking_start  = False
def onMouse(event, x, y, flags, param=None): # 마우스 이벤트에 의해 관심 영역 roi 설정.
     global roi
     global drag_start   # 마우스 클릭 위치.
     global mouse_status # 마우스 상태.
     global tracking_start    # 특징 추적을 위해 전역변수로 설정.
     if event == cv2.EVENT_LBUTTONDOWN:
          drag_start = (x, y)
          mouse_status = 1
          tracking_start = False
     elif event == cv2.EVENT_MOUSEMOVE:
          if flags == cv2.EVENT_FLAG_LBUTTON:
               xmin = min(x, drag_start[0])
               ymin = min(y, drag_start[1])
               xmax = max(x, drag_start[0])
               ymax = max(y, drag_start[1])
               roi = (xmin, ymin, xmax, ymax)
               mouse_status = 2 # dragging
     elif event == cv2.EVENT_LBUTTONUP:
          mouse_status = 3 # complete

#2          
cv2.namedWindow('tracking')
cv2.setMouseCallback('tracking', onMouse)

cap = cv2.VideoCapture('./data/checkBoard3x3.avi')
if (not cap.isOpened()): 
     print('Error opening video')
     
height, width = (int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
                 int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
roi_mask   = np.zeros((height, width), dtype=np.uint8)

params = dict(maxCorners=16,qualityLevel=0.001,minDistance=10,blockSize=5)
term_crit = (cv2.TERM_CRITERIA_MAX_ITER+cv2.TERM_CRITERIA_EPS,10,0.01)
params2 = dict(winSize= (5,5), maxLevel = 3, criteria =  term_crit)

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
     if mouse_status==2: # 마우스가 드래깅 상태면 frame에 빨간색 사각형 표시.
          x1, y1, x2, y2 = roi
          cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
#3-2          
     if mouse_status==3: # 마우스로 roi 설정을 완료하면 roi_mask에 roi 영역을 설정하고,
          print('initialize....')
          mouse_status = 0
          x1, y1, x2, y2 = roi
          roi_mask[:,:] = 0
          roi_mask[y1:y2, x1:x2] = 1
          p1 = cv2.goodFeaturesToTrack(imgC,mask=roi_mask,**params)   # 현재 프레임의 그레이스케일 영상 imgC의 roi 영역에서 특징점들을 p1에 검출.
          if len(p1)>=4:
               p1 = cv2.cornerSubPix(imgC, p1, (5,5),(-1,-1), term_crit)   # 부화소로 특징점 계산.
               rect = cv2.minAreaRect(p1)
               box_pts = cv2.boxPoints(rect).reshape(-1,1,2)
               tracking_start = True    # 특징점 추적 시작.
#3-3               
     if tracking_start:
          p2,st,err= cv2.calcOpticalFlowPyrLK(imgP,imgC,p1,None,**params2) # 이전 프레임 imgP에서 현재 프레임 imgC로의 특징점 p1의 각 좌표에서 광류 벡터를 p2에 계산.
          p1r,st,err=cv2.calcOpticalFlowPyrLK(imgC,imgP,p2,None,**params2) # 광류벡터가 올바르게 검출되었는지 확인하기 위하여 imgC에서 imgP로의 특징점 p2의 각 좌표에서 광류벡터를 p1r에 계산.
          d = abs(p1-p1r).reshape(-1, 2).max(-1)  # p1과 p1r 사이의 각 좌표의 거리를 x, y축에 대해 각각 계산하고 모든 좌표에서 최대값을 배열 d에 계산.
          stat = d < 1.0  # 1.0 is distance threshold. 1보다 작으면 True.
          good_p2 = p2[stat==1].copy()  # stat이 True인 좌표.
          good_p1 = p1[stat==1].copy()
          
          for x, y in good_p2.reshape(-1, 2):
               cv2.circle(frame, (int(x), int(y)), 3, (0,0,255), -1)
                
          if len(good_p2)<4:
               continue
          H, mask = cv2.findHomography(good_p1, good_p2, cv2.RANSAC, 3.0)  # good_p1에서 good_p2로의 투영변환 H 계산.
          box_pts = cv2.perspectiveTransform(box_pts, H)    # 마우스로 설정한 관심 영역 특징점 최소사각형의 모서리 좌표 box_pts에 투영변환 H를 적용하여 좌표변환.
          cv2.polylines(frame,[np.int32(box_pts)],True,(255,0, 0),2)
          p1 = good_p2.reshape(-1,1,2)  # 다음 프레임 추적을 위해 good_p2를 p1에 복사.

#3-4
     cv2.imshow('tracking',frame)
     imgP = imgC.copy()
     key = cv2.waitKey(25)
     if key == 27:
          break
if cap.isOpened():
     cap.release();
cv2.destroyAllWindows()
