#0310.py
import numpy as np
import cv2

width, height = 512, 512
x, y, R = 256, 256, 50
direction = 0 # right

while True:   
    key = cv2.waitKeyEx(30)     
    if key == 0x1B:     # Esc(0x1B)면 while문 종료.
        break;
    
# 방향키 방향전환 
    elif key == 0x270000: # right
        direction = 0
    elif key == 0x280000: # down
        direction = 1
    elif key == 0x250000: # left
        direction = 2
    elif key == 0x260000: # up
        direction = 3
        
# 방향으로 이동 
    if direction == 0:     # right
        x += 10
    elif direction == 1:   # down
        y += 10
    elif direction == 2:   # left
        x -= 10
    else: # 3, up
        y -= 10
        
#   경계확인 
    if x < R:
        x = R
        direction = 0
    if x > width - R:
        x = width - R
        direction = 2
    if y < R:
        y = R
        direction = 1
    if y > height - R:
        y = height - R
        direction = 3
        
# 지우고, 그리기        
    img = np.zeros((width, height,3), np.uint8) + 255 # 지우기
    cv2.circle(img, (x, y), R, (0, 0, 255), -1)     # (x,y) 위치에 원 그림.
    cv2.imshow('img', img)  # 영상을 화면에 표시. 조금씩 위치가 바뀌는 원의 모습이 착시를 일으켜 움직이는 것처럼 보임.
    
cv2.destroyAllWindows()
