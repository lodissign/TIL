# 0312.py
import numpy as np
import cv2

def onChange(pos):  # 트랙바 이벤트 핸들러 함수.
    global img      # 전역 변수로 참조.
    r = cv2.getTrackbarPos('R','img')   # trackbarname 'R', winname 'img' 트랙바에서 슬라이더의 현재 위치로부터 r 값을 얻는다.
    g = cv2.getTrackbarPos('G','img')
    b = cv2.getTrackbarPos('B','img')                   
    img[:] = (b, g, r)  # img 영상의 모든 화소를 (b,g,r) 색상으로 초기화.
    cv2.imshow('img', img)

# img = np.zeros((512, 512, 3), np.uint8)
img = np.zeros((700, 700, 3), np.uint8)
cv2.imshow('img',img)

# 트랙바 생성
cv2.createTrackbar('R', 'img', 0, 255, onChange)    # 윈도우에 트랙바 생성. value 0: 트랙바를 생성할 때 슬라이더의 위치, count 255: 슬라이더의 최대값, onChange() 함수: 슬라이더 위치가 변경될 때마다 슬라이더 이벤트 처리를 위해 호출될 함수.
cv2.createTrackbar('G', 'img', 0, 255, onChange)
cv2.createTrackbar('B', 'img', 0, 255, onChange)

# 트랙바 위치 초기화
#cv2.setTrackbarPos('R', 'img', 0)
#cv2.setTrackbarPos('G', 'img', 0)
cv2.setTrackbarPos('B', 'img', 255)

cv2.waitKey()
cv2.destroyAllWindows()
