import numpy as np, cv2, time

# # 1
# def pixel_access1(image):
#     image1 = np.zeros(image.shape[:2], image.dtype)
#     for i in range(image.shape[0]):
#         for j in range(image.shape[1]):
#             pixel = image[i,j]
#             image1[i,j] = 255 - pixel
#     return image1

# def pixel_access2(image):
#     image2 = np.zeros(image.shape[:2], image.dtype)
#     for i in range(image.shape[0]):
#         for j in range(image.shape[1]):
#             pixel = image[i,j]
#             image2.itemset((i, j), 255-pixel)
#     return image2

# def pixel_access3(image):
#     lut = [255 - i for i in range(256)]
#     lut = np.array(lut, np.uint8)
#     image3 = lut[image]
#     return image3

# def pixel_access4(image):
#     image4 = cv2.subtract(255, image)
#     return image4

# def pixel_access5(image):
#     image5 = 255 - image
#     return image5

# image = cv2.imread("ch06_images\\bright.jpg", cv2.IMREAD_GRAYSCALE)
# if image is None: raise Exception("영상 파일 읽기 오류 발생")

# # 수행시간 체크
# def time_check(func, msg):
#     start_time = time.perf_counter()
#     ret_img = func(image)
#     elapsed = (time.perf_counter() - start_time) * 1000
#     print(msg, "수행시간 : %.2f ms" % elapsed)
#     return ret_img

# image1 = time_check(pixel_access1, "[방법 1] 직접 접근 방식")
# image2 = time_check(pixel_access2, "[방법 2] item() 함수 방식")
# image3 = time_check(pixel_access3, "[방법 3] 룩업 테이블 방식")
# image4 = time_check(pixel_access4, "[방법 4] OpenCV 함수 방식")
# image5 = time_check(pixel_access5, "[방법 5] ndarray 연산 방식")

# # 결과 영상 보기
# cv2.imshow("image  - original", image)
# cv2.imshow("image1 - directly access to pixel", image1)
# cv2.imshow("image2 - item()/itemset()", image2)
# cv2.imshow("image3 - LUT", image3)
# cv2.imshow("image4 - OpenCV", image4)
# cv2.imshow("image5 - ndarray type", image5)
# cv2.waitKey(0)

# # 2
# image1 = np.zeros((50, 512), np.uint8)
# image2 = np.zeros((50, 512), np.uint8)
# rows, cols = image1.shape[:2]

# for i in range(rows):
#     for j in range(cols):
#         image1.itemset((i,j), j // 2)
#         image2.itemset((i,j), j // 20*10)

# cv2.imshow("image1", image1)
# cv2.imshow("image2", image2)
# cv2.waitKey(0)

# # 3
image = cv2.imread("ch06_images\pixel.jpg", cv2.IMREAD_GRAYSCALE) # 영상 읽기
if image is None:
    raise Exception("영상 파일 읽기 오류")

(x,y),(w,h) = (180, 37), (15, 10) # 좌표는 x, y
roi_img = image[y:y+h, x:x+w] # 행렬 접근은 y, x

#print(“[roi_img] =\n”, roi_img) # 행렬 원소 바로 출력 가능

print("[roi_img] =")
#print([roi_img])
for row in roi_img:
    for p in row:
        print("%4d" % p, end="") # 행렬 원 하나 출력
    print()

cv2.rectangle(image, (x,y, w,h), 255, 1)
cv2.imshow("image", image)
cv2.waitKey(0)
