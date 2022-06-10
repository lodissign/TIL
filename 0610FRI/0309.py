#0309.py
import numpy as np
import cv2

img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
text = 'OpenCV Programming'
org = (50,100)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,text, org, font, 1, (255,0,0), 2)   # text 문자열을 org 위치에 font 폰트, 폰트 스케일 1, 파란색, 두께 2로 출력. 

size, baseLine = cv2.getTextSize(text, font, 1, 2)  # text 문자열을 font 폰트, 폰트 스케일 1, 두께 2로 출력하기 위한 사각형의 크기를 size에 반환, baseLine은 맨 아래 텍스트 포인트를 기준으로 한 기준선의 y 좌표.
print('size=', size)
print('baseLine=', baseLine)
cv2.rectangle(img, org, (org[0]+size[0], org[1]-size[1]), (0, 0, 255))  # 사각형 모서리 좌표 org, (org[0]+size[0], org[1]-size[1])로 문자열의 출력 위치를 그린다. 실제 기준선의 y 좌표는 org[1]+baseLine.
cv2.circle(img, org, 3, (0, 255,0), 2)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
