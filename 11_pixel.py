import numpy as np, cv2, time

 # # 1
# image = cv2.imread("ch06_images\\bright.jpg", cv2.IMREAD_GRAYSCALE) # 영상 읽기
# if image is None: raise Exception("영상 파일 읽기 오류")

# # OpenCV 함수 이용
# dst1 = cv2.add(image, 100) # 영상 밝게 saturation 방식
# dst2 = cv2.subtract(image, 100) # 영상 어둡게

# # numpy array 이용
# dst3 = image + 100 # 영상 밝게 modulo 방식
# dst4 = image - 100 # 영상 어둡게

# cv2.imshow("original image", image)
# cv2.imshow("dst1- bright: OpenCV", dst1)
# cv2.imshow("dst2- dark: OpenCV", dst2)
# cv2.imshow("dst3- bright: numpy", dst3)
# cv2.imshow("dst4- dark: numpy", dst4)
# cv2.waitKey(0)

# # 2
# image1 = cv2.imread("ch06_images/add1.jpg", cv2.IMREAD_GRAYSCALE)
# image2 = cv2.imread("ch06_images/add2.jpg", cv2.IMREAD_GRAYSCALE)
# if image1 is None or image2 is None:
#     raise Exception("영상파일 읽기 오류")

# alpha, beta = 0.6, 0.7
# add_img1 = cv2.add(image1, image2)
# add_img2 = cv2.add(image1 * alpha, image2 * beta)
# add_img2 = np.clip(add_img2, 0, 255).astype('uint8')
# add_img3 = cv2.addWeighted(image1, alpha, image2, beta, 0)

# titles = ['image1', 'image2', 'add_img1', 'add_img2', 'add_img3']
# for t in titles:
#     cv2.imshow(t, eval(t))
# cv2.waitKey(0)

# # 3
# image = cv2.imread("ch06_images\contrast.jpg", cv2.IMREAD_GRAYSCALE)
# if image is None:
#     raise Exception("영상파일 읽기 오류")

# noimage = np.zeros(image.shape[:2], image.dtype)
# avg = cv2.mean(image)[0]/2.0

# dst1 = cv2.scaleAdd(image, 0.5, noimage)
# dst2 = cv2.scaleAdd(image, 2.0, noimage)
# dst3 = cv2.addWeighted(image, 0.5, noimage, 0, avg)
# dst4 = cv2.addWeighted(image, 2.0, noimage, 0, -avg)

# cv2.imshow("image", image)
# cv2.imshow("dst1 - decrease contrast", dst1)
# cv2.imshow("dst2 - decrease contrast", dst2)
# cv2.imshow("dst3 - decrease contrast using average", dst3)
# cv2.imshow("dst4 - decrease contrast using average", dst4)
# cv2.waitKey(0)

# # 4 히스토그램
def calc_histo(image, hsize, ranges = [0,256]): #행렬 원소의 1차원 히스토그램 계산
    hist = np.zeros((hsize, 1), np.float32) #히스토그램 누적 행렬
    gap = ranges[1]/hsize

    for i in range(image.shape[0]): #2차원 행렬 순회 방식
        for j in range(image.shape[1]):
            idx = int(image.item(i, j)/gap)
            hist[idx] += 1
    return hist

image = cv2.imread("ch06_images\pixel.jpg", cv2.IMREAD_GRAYSCALE) #영상일기
if image is None:
    raise Exception("영상 파일 읽기 오류") #히스토그램 간격수(범위), 값 범위

hsize, ranges = [32], [0, 256]
gap = ranges[1]/hsize[0]
ranges_gap = np.arange(0, ranges[1]+1, gap)
hist1 = calc_histo(image, hsize[0], ranges)
hist2 = cv2.calcHist([image], [0], None, hsize, ranges) #OpenCV 함수
hist3, bins = np.histogram(image, ranges_gap)

print("User 함수 : \n", hist1.flatten()) #행렬을 벡터로 변환해 출력
print("OpenCV 함수 : \n", hist2.flatten()) #행렬을 벡터로 변환해 출력
print("numpy 함수 : \n", hist3) #행렬을 벡터로 변환해 출력

cv2.imshow("image", image)
cv2.waitKey(0)