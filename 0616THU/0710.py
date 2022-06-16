# 0710.py
import cv2
import numpy as np

#1
src = cv2.imread('./data/hand.jpg')
##src = cv2.imread('./data/flower.jpg')
mask   = np.zeros(shape=src.shape[:2], dtype=np.uint8)  # 마우스로 지정할 마스크 영역을 지정하고 윤곽선을 검출할 영상 생성.
markers= np.zeros(shape=src.shape[:2], dtype=np.int32)  # 윤곽선을 이용하여 워터쉐드 분할을 위한 영상 생성.
dst = src.copy()
cv2.imshow('dst',dst)

#2
def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:  # 마우스 왼쪽 버튼을 누르고 움직이면,
            cv2.circle(param[0], (x, y), 10, (255, 255, 255), -1)   # param[0]에 반지름 10인 하얀색 원 그림.
            cv2.circle(param[1], (x, y), 10, (255, 255, 255), -1) 
    cv2.imshow('dst', param[1])    
##cv2.setMouseCallback('dst', onMouse, [mask, dst])

#3
mode = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE
while True:
    cv2.setMouseCallback('dst', onMouse, [mask, dst]) #3-1. 'dst' 윈도우에 onMouse() 이벤트 핸들러 설정.
    key = cv2.waitKey(30) # cv2.waitKeyEx(30)
    
    if key == 0x1B:     # Esc 키 누르면 종료.
        break;
    elif key == ord('r'): #3-2. r키 누르면 리셋.
        mask[:,:] = 0        # 모든 화소를 0으로 초기화.
        dst = src.copy()    # src를 dst에 깊은 복사.
        cv2.imshow('dst',dst)        
    elif key == ord(' '): #3-3. 스페이스바 누르면 영역 분할.
        temp, contours, hierarchy = cv2.findContours(mask, mode, method)
        print('len(contours)=', len(contours))
        markers[:,:] = 0  
        for i, cnt in enumerate(contours):
            cv2.drawContours(markers, [cnt], 0, i+1, -1)
        cv2.watershed(src,  markers)

        #3-4        
        dst = src.copy()
        dst[markers == -1] = [0,0,255] # 경계선
        for i in range(len(contours)): # 분할영역 
          r = np.random.randint(256)
          g = np.random.randint(256)
          b = np.random.randint(256)
          dst[markers == i+1] = [b, g, r]

        dst = cv2.addWeighted(src, 0.4, dst, 0.6, 0) # 합성
        cv2.imshow('dst',dst)        
cv2.destroyAllWindows()
