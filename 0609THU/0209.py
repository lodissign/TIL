# 0209.py
'''
 pip install youtube_dl
 pip install pafy
 pip 명령을 이용하여 유튜브 동영상을 다운로드 하는 기능이 있는 youtube_dl, pafy 패키지 설치.
'''
import cv2, pafy        # pafy 내부에서 youtube_dl 을 사용한다.
url = 'https://www.youtube.com/watch?v=u_Q7Dkl7AIk'
video = pafy.new(url)   # pafy.new()로 유튜브 url의 video 객체를 생성. 제목, 등급, 재생시간 등의 메타 데이터(데이터에 대한 데이터, 어떤 목적을 가지고 만들어진 데이터) 출력 가능.
print('title = ', video.title)
print('video.rating = ', video.rating)
print('video.duration = ', video.duration)

best = video.getbest() # video.getbest(preftype='mp4'). 최적의 비디오 파일양식 정보를 best에 저장,
print('best.resolution', best.resolution)

cap=cv2.VideoCapture(best.url)  # best.url 을 이용하여 VideoCapture 객체 cap 생성.
while(True):
        retval, frame = cap.read()      # cap.read()로 비디오 프레임 frame을 캡처하여 창에 표시하고,
        if not retval:
                break
        cv2.imshow('frame',frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # cv2.cvtColor()로 그레이스케일로 변환하고, 
        edges = cv2.Canny(gray,100,200)                 # cv2.Canny()로 에지를 검출하여 창에 표시.
        cv2.imshow('edges',edges)

        key = cv2.waitKey(25)
        if key == 27: # Esc
                break
cv2.destroyAllWindows()
