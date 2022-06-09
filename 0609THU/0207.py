# 0207.py
import cv2

# cap = cv2.VideoCapture(0)  # 0번 카메라에 대한 VideoCapture 객체 cap을 생성. 
cap = cv2.VideoCapture('./data/vtest.avi')  # 비디오 파일 'vtest.avi'로부터 VideoCapture 객체를 생성할 수도 있다.
##cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
##cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),   
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))  
# cap.get()으로 비디오 프레임의 가로, 세로 크기 속성을 읽어 정수로 변환하여 frame_size에 할당. 비디오 파일 'vtest.avi'는 frame_size=(768, 576)이다. 
# 카메라의 경우 cap.set()으로 비디오 프레임의 가로, 세로 크기 속성을 변경할 수 있다. 속성은 카메라의 성능에 의존한다.

print('frame_size =', frame_size)

while True:   
    retval, frame = cap.read()  # 비디오 프레임을 frame에 캡처.
    if not retval:  # 프레임 캡처에 실패(retval=False)하면 break 문에 의해 비디오 프레임 캡처를 중지시키기 위하여 반복을 중단한다.
        break

    cv2.imshow('frame',frame)   # 프레임을 캡처(retval=True)하면 imshow()로 'frame' 윈도우에 입력 비디오 프레임 frame을 표시한다.
    
    key = cv2.waitKey(25)   # 25/1000초 대기시간을 갖고,
    if key == 27: # Esc     # 입력된 key가 Esc이면 while문을 탈출, 
        break
if cap.isOpened():           
    cap.release()           # 비디오 객체 cap을 해제한 뒤, 
cv2.destroyAllWindows()     # 모든 윈도우 파괴, 프로그램 종료.
