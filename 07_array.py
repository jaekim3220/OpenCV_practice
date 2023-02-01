import numpy as np
import cv2

# image = cv2.imread("ch05_images/flip_test.jpg", cv2.IMREAD_COLOR)
# if image is None: #예외처리
#     raise Exception("영상파일 읽기 오류 발생")

# x_axis = cv2.flip(image, 0) #x축 기준 상하
# y_axis = cv2.flip(image, 1) #y축 기준 좌우
# xy_axis = cv2.flip(image, -1) 
# rep_image = cv2.repeat(image, 1, 2) #반복 복사
# trans_image = cv2.transpose(image) #행렬 전치

# # 각 행렬을 영상으로 표시
# titles = ['image', 'x_axis','y_axis', 'xy_axis', 'rep_image', 'trans_image']
# for title in titles:
#     cv2.imshow(title, eval(title))
# cv2.waitKey(0)

# # 채널 처리 함수(행렬)
# ch0 = np.zeros((2,4), np.uint8) + 10 #0 원소 행렬 선언 후 10+
# ch1 = np.ones((2,4), np.uint8) * 20 #1 원소 행렬 선언 후 * 20
# ch2 = np.full((2,4), 30, np.uint8) #행렬을 생성해 30으로 초기화

# list_bgr = [ch0, ch1, ch2] #단일채널 행렬들을 모아 리스트 구성
# merge_bgr = cv2.merge(list_bgr) #채널 합성
# split_bgr = cv2.split(merge_bgr) #채널 분리 : 컬러 영상 -> 3채널 분리

# print("split_bgr 행렬 형태", np.array(split_bgr).shape)
# print("merge_bgr 행렬 형태", merge_bgr.shape)
# print("[ch0] = \n%s" % ch0) #단일채널 원소 출력
# print("[ch1] = \n%s" % ch1)
# print("[ch2] = \n%s\n" % ch2)
# print("[merge_bgr] = \n %s\n" % merge_bgr) #다채널 원소 출력

# print("[split_bgr[0]] = \n%s" % split_bgr[0]) #분리 채널 결과 출력
# print("[split_bgr[1]] = \n%s" % split_bgr[1])
# print("[split_bgr[2]] = \n%s" % split_bgr[2])

# # 컬러 채널 분리
image = cv2.imread("ch05_images\color.jpg", cv2.IMREAD_COLOR) #영상 읽기
if image is None: #예외 처리
    raise Exception("영상 파일 읽기 오류")
if image.ndim != 3: #예외 처리-컬러 영상 확인
    raise Exception("컬러 영상 아님")

bgr = cv2.split(image) #채널 분리 : 컬러 영상 -> 3채널 분리
# blue, green, red = cv2.split(image) #3개 변수로 반환받기 가능
print("bgr 자료형 : ", type(bgr), type(bgr[0]), type(bgr[0][0][0]))
print("bgr 원소 개수 : ", len(bgr))

# 각 채널을 윈도우에 띄우기
cv2.imshow("image", image)
cv2.imshow("Blue Channel", bgr[0]) #Blue 채널
cv2.imshow("Green Channel", bgr[1]) #Green 채널
cv2.imshow("Red Channel", bgr[2]) #Red 채널
# cv2.imshow("Blue Channel", image[:,:,0]) #넘파이 객체 인덱싱 방식
# cv2.imshow("Green Channel", image[:,:,1])
# cv2.imshow("Red Channel", image[:,:,2])
cv2.waitKey(0)
# bgr 자료형 : <bgr 자료형><bgr 원소 단일채널 자료형><단일채널의 원소 자료형> 으로 나옴