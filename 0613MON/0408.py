# 0408.py
import cv2
 
src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
rects = cv2.selectROIs('src', src, False, True) # 'src' 윈도우에 src 영상을 표시, showCrosshair= False로 선택영역에 격자를 표시하지 않고, fromCenter= True로 마우스 클릭 위치 중심을 기준으로 드래그하여 박스를 선택, 스페이스바/엔터키를 눌러 반복적으로 ROI를 지정, Esc키를 눌러 다중 영역 선택을 종료하면 rects에 반환.
print('rects =', rects)

for r in rects:
    cv2.rectangle(src, (r[0], r[1]), (r[0]+r[2], r[1]+r[3]), 255)    # 각각의 ROI 영역 r을 이용하여 src 영상에 사각형 표시.
##    img = src[r[1]:r[1]+r[3], r[0]:r[0]+r[2]]
##    cv2.imshow('Img', img)
##    cv2.waitKey()

cv2.imshow('src', src)
cv2.waitKey()    
cv2.destroyAllWindows()
