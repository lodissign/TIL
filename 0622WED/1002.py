# 1002.py
import cv2
import numpy as np

#1
cap = cv2.VideoCapture('./data/vtest.avi')
if (not cap.isOpened()): 
     print('Error opening video')
     
height, width = (int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
              int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))

TH      = 40  # binary threshold. 이진 영상 임계값.
AREA_TH = 80 # area   threshold. 면적 임계값.
bkg_gray= cv2.imread('./data/avg_gray.png', cv2.IMREAD_GRAYSCALE)
bkg_bgr = cv2.imread('./data/avg_bgr.png')

mode = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE

#2
# 비디오 프레임을 획득하고, 
# 컬러영상 frame, 그레이스케일 영상 gray의 배경 영상으로부터의 절대값 차영상을 diff_gray와 diff_bgr에 계산, 
# 임계값 AREA_TH에 의한 이진 영상 계산, 윤곽선 계산, 면적 AREA_TH보다 큰 윤곽선의 바운딩 사각형으로 이동물체(사람) 검출.

t = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    t+=1
    print('t =', t)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
#2-1 
    diff_gray  = cv2.absdiff(gray, bkg_gray)    # gray와 bkg_gray의 그레이 배경 차영상 계산.
##    ret, bImage= cv2.threshold(diff_gray,TH,255,cv2.THRESH_BINARY)    # 임계값 TH로 이진 영상 bImage 계산, 모폴로지 연산으로 잡음을 제거하여 물체와 배경을 분할하는 이진 영상을 생성.
    
#2-2      
    diff_bgr = cv2.absdiff(frame, bkg_bgr)      
    db, dg, dr = cv2.split(diff_bgr)
    ret, bb = cv2.threshold(db,TH,255,cv2.THRESH_BINARY)
    ret, bg = cv2.threshold(dg,TH,255,cv2.THRESH_BINARY)
    ret, br = cv2.threshold(dr,TH,255,cv2.THRESH_BINARY)
 
    bImage = cv2.bitwise_or(bb, bg)
    bImage = cv2.bitwise_or(br, bImage)
      
    bImage = cv2.erode(bImage, None, 5)
    bImage = cv2.dilate(bImage,None, 5)    
    bImage = cv2.erode(bImage, None, 7)

#2-3     
    contours, hierarchy = cv2.findContours(bImage, mode, method)    # bImage에서 윤곽선 contours 검출.
    cv2.drawContours(frame, contours, -1, (255,0,0), 1)   
    for i, cnt in enumerate(contours):
        area = cv2.contourArea(cnt) # 각 윤곽선 cnt의 면적이 AREA_TH보다 큰 윤곽선의 바운딩 사각형을 frame에 빨간색 표시.
        if area > AREA_TH:
            x, y, width, height = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+width, y+height), (0,0,255), 2)
    
    cv2.imshow('frame',frame)
    cv2.imshow('bImage',bImage)
    cv2.imshow('diff_gray',diff_gray)
    cv2.imshow('diff_bgr',diff_bgr)
    key = cv2.waitKey(25)
    if key == 27:
        break
#3
if cap.isOpened():
    cap.release();
cv2.destroyAllWindows()
