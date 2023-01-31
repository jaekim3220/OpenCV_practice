import cv2

# # 연습문제_6
# cap = cv2.VideoCapture(0) # Open the webcam

# while True:
#     ret, frame = cap.read() # Read a frame from the webcam
#     if cap.isOpened() == False:
#         raise Exception("카메라 연결 안됨")
    
#     # Define the area of interest
#     roi = frame[200:400, 100:200]
#     # Increase the green component in the area of interest
#     roi[:, :, 1] += 50
#     # Merge the modified area of interest back into the original frame
#     frame[200:400, 100:200] = roi
#     # Draw a red rectangle around the area of interest with thickness 3
#     cv2.rectangle(frame, (100, 200), (200, 400), (0, 0, 255), 3)
#     frame = cv2.flip(frame, 1) # 좌우 반전
#     cv2.imshow("Webcam", frame) # Show the resulting frame
    
#     # Check if the 'ESC' key is pressed
#     key = cv2.waitKey(1)
#     if key == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()

# # 연습문제_7

cap = cv2.VideoCapture(0)

# 영상 코드, fps 설정
fourcc = cv2.VideoWriter_fourcc(*"DIVX")
fps = 15

# 영상 크기 설정, VideoWriter object 생성
width = 600
height = 480
out = cv2.VideoWriter('video/Flip_test.avi', fourcc, fps, (width, height))

while True:
    # 웹캠으로 영상 녹화
    ret, frame = cap.read()

    # 좌우 반전
    frame = cv2.flip(frame, 1)

    # 좌우 반전 영상을 VideoWriter에 기록합니다
    out.write(frame)

    # 녹화 화면 띄우기
    cv2.imshow("Flip Test", frame)

    if cv2.waitKey(1) == 27: # esc로 중단
        break

# 중지
out.release()
cap.release()
cv2.destroyAllWindows()