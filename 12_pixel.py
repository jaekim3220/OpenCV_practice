import numpy as np, cv2

# def draw_histo(hist, shape=(200,256)):
#     hist_img = np.full(shape, 255, np.uint8)
#     cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX) #정규화
#     gap = hist_img.shape[1]/hist.shape[0]

#     for i, h in enumerate(hist):
#         x = int(round(i*gap))
#         w = int(round(gap))
#         cv2.rectangle(hist_img, (x, 0, w, int(h)), 0, cv2.FILLED)

#     return cv2.flip(hist_img, 0) #영상 상하 뒤집기 후 반환

# image = cv2.imread("ch06_images\pixel.jpg", cv2.IMREAD_GRAYSCALE)
# if image is None:
#     raise Exception("영상 파일 읽기 오류")
    
# hist = cv2.calcHist([image], [0], None, [32], [0, 256])
# hist_img = draw_histo(hist)

# cv2.imshow("image", image)
# cv2.imshow("hist_img", hist_img)
# cv2.waitKey(0)

# # 2 컬러 공간 변환(BGR->CMY)
# BGR_img = cv2.imread("ch06_images\color_model.jpg", cv2.IMREAD_COLOR)
# if BGR_img is None:
#     raise Exception("영상 파일 읽기 오류")

# white = np.array([255, 255, 255], np.uint8)
# CMY_img = white - BGR_img
# yellow, magenta, cyan = cv2.split(CMY_img)

# titles = ['BGR_img', 'CMY_img', 'yellow', 'magenta', 'cyan']
# for t in titles:
#     cv2.imshow(t, eval(t))
# cv2.waitKey(0)

# # 3
# def onThreshold(value):
#     result = cv2.threshold(image, value, 255, cv2.THRESH_BINARY_INV)[1] 
#     #cv2.THRESH_BINARY -> (cv2.THRESH_BINARY_INV,cv2.THRESH_TOZERO,cv2.THRESH_TOZERO_INV)
#     cv2.imshow("result", result)

# image = cv2.imread("ch06_images\color_space.jpg", cv2.IMREAD_GRAYSCALE) #컬러 영상 읽기
# if image is None:
#     raise Exception("영상 파일 읽기 오류")

# cv2.namedWindow("result")
# cv2.createTrackbar("threshold", "result", 128, 255, onThreshold)
# onThreshold(128) #이진화 수행
# cv2.imshow("image", image)
# cv2.waitKey(0)

# # 4
def onThreshold(value):
    th[0] = cv2.getTrackbarPos("Hue_th1", "result")
    th[1] = cv2.getTrackbarPos("Hue_th1", "result")
    _, result = cv2.threshold(hue, th[1], 255, cv2.THRESH_TOZERO_INV)
    cv2.threshold(result, th[0], 255, cv2.THRESH_BINARY, result)
    cv2.imshow("result", result)

BGR_img = cv2.imread("ch06_images\color_space.jpg", cv2.IMREAD_COLOR)
if BGR_img is None:
    raise Exception("영상 파일 읽기 오류")

HSV_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2HSV)
hue = np.copy(HSV_img[:, :, 0])
th = [50, 100]

cv2.namedWindow("result")
cv2.createTrackbar("Hue_th1", "result", th[0], 255, onThreshold)
cv2.createTrackbar("Hue_th2", "result", th[1], 255, onThreshold)
onThreshold(th[0])
cv2.imshow("BGR_img", BGR_img)
cv2.waitKey(0)

# # 5


# # 6


# # 7 
def filter(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32) # 회선 결과 저장 행렬
    xcenter, ycenter = mask.shape[1]//2, mask.shape[0]//2  # 마스크 중심 좌표
    print(xcenter), print(ycenter)

    #for i in range(ycenter, rows - ycenter):  # 입력 행렬 반복 순회
    #    for j in range(xcenter, cols - xcenter):
    for i in range(1, rows-1): # 입력 행렬 반복 순회
        for j in range(1, cols-1 ):
            y1, y2 = i - ycenter, i + ycenter + 1 # 관심영역 높이 범위
            x1, x2 = j - xcenter, j + xcenter + 1 # 관심영역 너비 범위
            roi = image[y1:y2, x1:x2].astype("float32") # 관심영역 형변환

            tmp = cv2.multiply(roi, mask) # 회선 적용 - OpenCV 곱셈
            dst[i, j] = cv2.sumElems(tmp)[0] # 출력화소 저장
    return dst   

# # 8 예제 7.1.2




