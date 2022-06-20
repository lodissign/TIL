# 0902.py
import cv2
import numpy as np
 
src = cv2.imread('./data/chessBoard.jpg')
gray= cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

#1
fastF = cv2.FastFeatureDetector_create()
kp = fastF.detect(gray) 
dst = cv2.drawKeypoints(gray, kp, None, color=(255,0,0))
print('len(kp)=', len(kp))

#2
kp = sorted(kp, key=lambda f: f.response, reverse=True) # 특징점 kp를 내림차순으로 정렬.
cv2.drawKeypoints(gray, kp[:10], dst, color=(0,0,255),
                 flags = cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG)   # 반응값이 큰 10개 kp[:10] 모든 특징점을 파란색 원으로 그림.
cv2.imshow('dst',  dst)

#3
kp2 = list(filter(lambda f: f.response>50, kp)) # OpenCV_python은 KeypointFilter를 사용할 수 없기 때문에 직접 특징점 필터링 작성. 반응값이 50보다 작은 특징은 제거하여 kp2 생성.
print('len(kp2)=', len(kp2))
##for f in kp2:
##    print(f.response)

dst2 = cv2.drawKeypoints(gray, kp2, None, color=(0,0,255))   
cv2.imshow('dst2',  dst2)

#4
def distance(f1, f2):    
    x1, y1 = f1.pt
    x2, y2 = f2.pt
    return np.sqrt((x2 - x1)**2+ (y2 - y1)**2)

def filteringByDistance(kp, distE=0.5): # 반응값 기준으로 내림차순 정렬된 특징점 kp에서 거리오차 distE 보다 작은 특징점은 삭제.
    size = len(kp)
    mask = np.arange(1,size+1).astype(np.bool8) # all True   
    for i, f1 in enumerate(kp):
        if not mask[i]:
            continue
        else: # True
            for j, f2 in enumerate(kp):
                if i == j:
                    continue
                if distance(f1, f2)<distE:
                    mask[j] = False
    np_kp = np.array(kp)
    return list(np_kp[mask])

kp3 = filteringByDistance(kp2, 30)
print('len(kp3)=', len(kp3))
dst3 = cv2.drawKeypoints(gray, kp3, None, color=(0,0,255))
cv2.imshow('dst3',  dst3)
cv2.waitKey()
cv2.destroyAllWindows()
