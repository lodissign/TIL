# 1003.py
import cv2
import numpy as np

#1
cap = cv2.VideoCapture('./data/vtest.avi')
if (not cap.isOpened()): 
     print('Error opening video')
     
height, width = (int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
                 int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))

TH      = 40  # binary threshold
AREA_TH = 80 # area   threshold 
acc_bgr = np.zeros(shape=(height, width, 3), dtype=np.float32)

mode = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE

#2
t = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    t+=1
    print("t = ", t)
    blur = cv2.GaussianBlur(frame,(5,5),0.0)    # 컬러 영상 frame을 가우시안 블러링.
#2-1
    if t < 50:
        cv2.accumulate(blur, acc_bgr)   # t<50 일때까지는 입력 영상을 누적.
        continue    # 다음 프레임 획득.
    elif t == 50:
        bkg_bgr = acc_bgr/t # 평균 영상으로 배경 영상 계산.
#2-2: t >= 50 에서는 컬러 배경 차영상으로 이동물체(사람)를 검출, 이동평균을 사용하여 배경 영상을 갱신.
##    diff_bgr = cv2.absdiff(np.float32(blur), bkg_bgr).astype(np.uint8)
    diff_bgr = np.uint8(cv2.absdiff(np.float32(blur), bkg_bgr))
    db,dg,dr = cv2.split(diff_bgr)
    ret, bb = cv2.threshold(db,TH,255,cv2.THRESH_BINARY)
    ret, bg = cv2.threshold(dg,TH,255,cv2.THRESH_BINARY)
    ret, br = cv2.threshold(dr,TH,255,cv2.THRESH_BINARY)
    bImage = cv2.bitwise_or(bb, bg)
    bImage = cv2.bitwise_or(br, bImage)
    bImage = cv2.erode(bImage,None, 5)
    bImage = cv2.dilate(bImage,None,5)    
    bImage = cv2.erode(bImage,None, 7)
    cv2.imshow('bImage',bImage)
    msk = bImage.copy()
    contours, hierarchy = cv2.findContours(bImage, mode, method)
    cv2.drawContours(frame, contours, -1, (255,0,0), 1)   
    for i, cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        if area > AREA_TH:
            x, y, width, height = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+width, y+height), (0,0,255), 2)
            cv2.rectangle(msk, (x, y), (x+width, y+height), 255, -1) 
#2-3
    msk = cv2.bitwise_not(msk)  # 이동물체 영역은 0, 배경은 255로 반전.
    cv2.accumulateWeighted(blur,bkg_bgr, alpha=0.1,mask=msk)    # 이동평균을 0.1 x blur + bkg_bgr로 계산하여 마스크 msk에서 255인 배경에서만 갱신.

    cv2.imshow('frame',frame)
    cv2.imshow('bkg_bgr',np.uint8(bkg_bgr))    
    cv2.imshow('diff_bgr',diff_bgr)
    key = cv2.waitKey(25)
    if key == 27:
        break
#3
if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
