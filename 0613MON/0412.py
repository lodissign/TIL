# 0412.py
import cv2
src = cv2.imread('./data/lena.jpg')

b, g, r = cv2.split(src)    # 3-채널 컬러 영상 src를 채널 분리하여 b,g,r,에 저장.
dst = cv2.merge([b, g, r])  # 리스트 [b,g,r]을 dst에 채널 합성. cv2.merge([r,g,b]) 는 다른 색상의 컬러 영상을 생성한다.
dst2 = cv2.merge([r,g,b])

print(type(dst))    
print(dst.shape)    # dst.shape=(512,512,3)로 dst는 src와 같은 3-채널 컬러 영상.
cv2.imshow('dst',  dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()    
cv2.destroyAllWindows()
