import numpy as np
import cv2

# def put_string(frame, text, pt, value, color = (120,200,90)):
#     text += str(value)
#     shade = (pt[0]+2, pt[1]+2)
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     cv2.putText(frame, text, shade, font, 0.7, (0,0,0),2)
#     cv2.putText(frame,text,pt,font,0.7,color,2)

# capture = cv2.VideoCapture(0)
# if capture.isOpened() == False:
#     raise Exception("카메라 연결 안됨")

# print("너비 %d" % capture.get(cv2.CAP_PROP_FRAME_WIDTH))
# print("높이 %d" % capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
# print("노출 %d" % capture.get(cv2.CAP_PROP_EXPOSURE))
# print("밝기 %d" % capture.get(cv2.CAP_PROP_BRIGHTNESS))

# while True:
#     ret, frame = capture.read()
#     if not ret:
#         break
#     if cv2.waitKey(30) >= 0:
#         break
#     exposure = capture.get(cv2.CAP_PROP_EXPOSURE)
#     frame = cv2.flip(frame, 1) # Flip the frame left-right
#     put_string(frame, 'EXPOS : ', (10,40), exposure)
#     title = "View Frame Frome Camera"
#     cv2.imshow(title, frame)
# capture.release()

'''카메라 속성 설정, 캡쳐(압축 영상)'''
from Common.utils import put_string #함수 재사용 코드

def zoom_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_ZOOM, value)

def focus_bar(value): #줌 조절 콜백 함수
    global capture
    capture.set(cv2.CAP_PROP_FOCUS, value) # 줌 설정

capture = cv2.VideoCapture(0)
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨") # 예외

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400) # 프레임 너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300) # 프레임 높이
capture.set(cv2.CAP_PROP_AUTOFOCUS, 0) # 자동초점 중지
capture.set(cv2.CAP_PROP_BRIGHTNESS, 100) #프레임 밝기 초기화

title = "Change Camera Properties" # 윈도우 이름 지정
cv2.namedWindow(title) # 윈도우 생성
cv2.createTrackbar('zoom', title, 0, 10, zoom_bar) # 줌 트랙바
cv2.createTrackbar('focus', title, 0, 40, focus_bar) # 포커스 트랙바

while True:
    ret, frame = capture.read()
    if not ret:
        break
    if cv2.waitKey(30) >= 0:
        break

    zoom = cv2.getTrackbarPos("zoom", title)
    focus = cv2.getTrackbarPos("focus", title)
    frame = cv2.flip(frame, 1) # 좌우 반전
    put_string(frame, 'zoom : ', (10, 240), zoom)
    put_string(frame, 'focus : ', (10, 270), focus)
    cv2.imshow(title,frame)
capture.release()