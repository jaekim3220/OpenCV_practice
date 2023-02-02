import numpy as np, cv2

# #예제 7.2.5
# from Common.filters import differential

# image = cv2.imread("ch07_images\edge.jpg", cv2.IMREAD_GRAYSCALE)
# if image is None:
#     raise Exception("영상 파일 읽기 오류")

# data1 = [-1, 0, 1,
#         -2, 0, 2,
#         -1, 0, 1]
# data2 = [-1, -2, -1,
#         0, 0, 0,
#         1, 2, 1]
# dst, dst1, dst2 = differential(image, data1, data2)

# dst3 = cv2.Sobel(np.float32(image), cv2.CV_32F, 1,0,3)
# dst4 = cv2.Sobel(np.float32(image), cv2.CV_32F, 0,1,3)
# dst3 = cv2.convertScaleAbs(dst3)
# dst4 = cv2.convertScaleAbs(dst4)

# cv2.imshow("dst1- vertical_mask", dst1)
# cv2.imshow("dst2- horizontal_mask", dst2)
# cv2.imshow("dst3- vertical_mask", dst3)
# cv2.imshow("dst4- horizontal_mask", dst4)
# cv2.waitKey(0)

# # 예제 7.2.6



# # 예제 7.3.2 평균값 필터링
# image = cv2.imread("ch07_images\\filter_avg.jpg", cv2.IMREAD_GRAYSCALE)
# if image is None:
#     raise Exception("영상파일 읽기 오류")

# blur_img = cv2.blur(image, (5,5), borderType=cv2.BORDER_CONSTANT)
# box_img = cv2.boxFilter(image, ddepth = -1, ksize=(5,5))

# cv2.imshow("image", image),
# cv2.imshow("blur_img", blur_img)
# cv2.imshow("box_img", box_img)
# cv2.waitKey(0)

# # 예제 7.3.5 블러링&캐니에지
# def onTrackbar(th):
#     rep_edge = cv2.GaussianBlur(rep_gray, (5,5), 0)
#     red_edge = cv2.Canny(rep_edge, th, th*2, 5)
#     h, w = image.shape[:2]
#     cv2.rectangle(rep_edge, (0,0,w,h),255,-1)
#     color_edge = cv2.bitwise_and(rep_image, rep_image, mask=rep_edge)
#     cv2.imshow("color edge", color_edge)

# image = cv2.imread("ch07_images\edge.jpg", cv2.IMREAD_COLOR)
# if image is None:
#     raise Exception("영상파일 읽기 오류")

# th = 50
# rep_image = cv2.repeat(image, 1, 2)
# rep_gray = cv2.cvtColor(rep_image, cv2.COLOR_BGR2GRAY)

# cv2.namedWindow("color edge", cv2.WINDOW_AUTOSIZE)
# cv2.createTrackbar("Canny th", "color edge", th, 100, onTrackbar)
# onTrackbar(th)
# cv2.waitKey(0)

# # 예제 7.4.1 침식 연산(노이즈 제거)
image = cv2.imread("ch07_images\morph.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상 파일 읽기 오류")

data = [0,1,0,
        1,1,1,
        0,1,0]
mask = np.array(data, np.uint8).reshape(3,3) #마스크 선언 및 초기화
th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1] #영상 이진화

dst2 = cv2.erode(th_img, mask)

cv2.imshow("image", image)
cv2.imshow("binary image", th_img)
cv2.imshow("OpenCV erode", dst2)
cv2.waitKey(0)

# # 예제 7.4.2 팽창 연산(객체 내부 잡음 제거, 배경 잡을 증가)
image = cv2.imread("ch07_images\morph.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상 파일 읽기 오류")

#마스크 초기화
mask = np.array([[0,1,0],
                [1,1,1],
                [0,1,0]]).astype("uint8")
th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1] #영상 이진화

dst2 = cv2.morphologyEx(th_img, cv2.MORPH_DILATE, mask) #OpenCV 팽창 함수

cv2.imshow("OpenCV dilate", dst2)
cv2.waitKey(0)

# # 예제 7.4.3 열림/닫힘 연산(침식/팽창 연산 조절) 닫힘 : 팽창->침식
