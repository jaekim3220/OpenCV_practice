import cv2

# capture = cv2.VideoCapture(0)
# if capture.isOpened() == False:
#     raise Exception("카메라 연결 안됨")

# fps = 29.92 #초당 프레임
# delay = round(1000/fps) #프레임
# size = (640, 360) #동영상파일 
# fourcc = cv2.VideoWriter_fourcc(*'DX50') #압축 코덱 설정

# #카메라 속성 실행창에 출력
# print("width * height : ", size)
# print("VideoWriterfourcc : %s" % fourcc)
# print("delay : %2d ms" % delay)
# print("fps : %.2f" % fps)

# capture.set(cv2.CAP_PROP_ZOOM, 1)
# capture.set(cv2.CAP_PROP_FOCUS, 0)
# capture.set(cv2.CAP_PROP_FRAME_WIDTH, size[0]) #해상도 결정
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1])

# # 동영상 파일 개방 및 코덱, 해상도 설정
# # Common 파일에 저장
# writer = cv2.VideoWriter("images/video_file.avi", fourcc, fps, size)
# if writer.isOpened() == False:
#     raise Exception("동영상 파일 개방 안됨")

# while True:
#     ret, frame = capture.read() #카메라 영상 받기
#     if not ret:
#         break
#     if cv2.waitKey(delay) >= 0:
#         break
#     frame = cv2.flip(frame, 1) # 좌우 반전
#     writer.write(frame) #프레임을 동영상으로 저장
#     cv2.imshow("View Frame From Camera", frame)

# writer.release()
# capture.release()

# 동영상파일 실행(특정 프레임 이후 색 변환)
from Common.utils import put_string #글쓰기 함수 임포트

capture = cv2.VideoCapture("images/video_file.avi") #동영상파일 개방
if not capture.isOpened():
    raise Exception("동영상 파일 개방 안됨") #예외 처리

frame_rate = capture.get(cv2.CAP_PROP_FPS) #초당 프레임 수
delay = int(1000/frame_rate) #지연 시간
frame_cnt = 0 #현재 프레임 번호

while True:
    ret, frame = capture.read()
    if not ret or cv2.waitKey(delay) >= 0: #프레임 간 지연 시간 지정
        break
    blue, green, red = cv2.split(frame) #컬러 영상 채널 분리
    frame_cnt += 1

    if 100 <= frame_cnt < 200: #blue 채널 밝기 증가
        cv2.add(blue, 100, blue)
    elif 200 <= frame_cnt <300: #green 채널 밝기 증가
        cv2.add(green, 100, green)
    elif 300 <- frame_cnt <400: #red 채널 밝기 증가
        cv2.add(red, 100, red)

    frame = cv2.merge([blue, green, red]) #단일채널 영상 합셩
    put_string(frame, 'frame_cnt : ', (20, 30), frame_cnt)
    cv2.imshow("Read Video File", frame)
capture.release()