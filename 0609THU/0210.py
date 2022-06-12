# 0210.py
import cv2

cap = cv2.VideoCapture(1) # 0번 카메라
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size =', frame_size)

#fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # ('D', 'I', 'V', 'X')
fourcc = cv2.VideoWriter_fourcc(*'XVID')    # VideoWriter_fourcc(*'XVID')로 비디오 출력을 위한 코덱을 4-문자로 fourcc에 생성.

out1 = cv2.VideoWriter('./data/record0.mp4',fourcc, 20.0, frame_size)   # 비디오 파일 'record0.mp4', 코덱 fourcc, 프레임 속도 fps 20.0, 프레임 크기 frame_size, 컬러 영상 여부 isColor=True로 설정하여 컬러 비디오 VideoWriter 객체 out1을 생성.
out2 = cv2.VideoWriter('./data/record1.mp4',fourcc, 20.0, frame_size,isColor=False) # 비디오 파일 'record1.mp4', 코덱 fourcc, 프레임 속도 fps 20.0, 프레임 크기 frame_size, 컬러 영상 여부 isColor=False로 설정하여 그레이스케일 비디오 VideoWriter 객체 out2를 생성.

while True: # 무한 반복하는 while문에서 retval, frame=cap.read()로 비디오 프레임을 캡처하고, 
    retval, frame = cap.read()
    if not retval:
        break   
    out1.write(frame)   # out1.write(frame)로 frame을 out1 객체에 출력, 
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # cvtColor()로 입력 비디오 프레임을 그레이스케일 영상으로 gray에 변환, 
    out2.write(gray)    # gray를 out2 객체에 출력.
    cv2.imshow('frame',frame) 
    cv2.imshow('gray',gray)      
    
    key = cv2.waitKey(25)   
    if key == 27:       # Esc 입력 경우 while 문 탈출.
        break
cap.release()
out1.release()
out2.release()
cv2.destroyAllWindows()
