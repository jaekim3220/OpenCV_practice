import numpy as np, cv2

# # 8.3.2 양선형 보간법
# image = cv2.imread("ch08_images\interpolation.jpg", cv2.IMREAD_GRAYSCALE)
# if image is None:
#     raise Exception("영상 파일 읽기 오류")

# size = (350, 400)
# dst3 = cv2.resize(image, size, cv2.INTER_LINEAR) #INTER_NEAREST, INTER_LINEAR, 
# dst4 = cv2.resize(image, size, cv2.INTER_NEAREST) #INTER_CUBIC, INTER_AREA, INTER_LANCZOS4

# cv2.imshow("image", image)
# cv2.imshow("OpenCV_bilinear", dst3)
# cv2.imshow("OpenCV_Nearest", dst4)
# cv2.waitKey(0)

# # 8.4 평행이동
# def contain(p, shape):
#     return 0<= p[0] < shape[0] and 0<= p[1] < shape[1]

# def translate(img, pt):
#     dst = np.zeros(img.shape, img.dtype)
#     for i in range(img.shape[0]):
#         for j in range(img.shape[1]):
#             x, y = np.subtract((j, i), pt)
#             if contain((y, x), img.shape):
#                 dst[i, j] = img[y, x]
#     return dst

# image = cv2.imread("ch08_images\\translate.jpg", cv2.IMREAD_GRAYSCALE)
# if image is None:
#     raise Exception("영상 파일 읽기 오류")

# dst1 = translate(image, (30, 80))
# dst2 = translate(image, (-70, -50))

# cv2.imshow("image", image)
# cv2.imshow("dst1 : transted to (30, 80)", dst1)
# cv2.imshow("dst2 : transted to (-70, -50)", dst2)
# cv2.waitKey(0)

# # 8.4 평행이동2
image = cv2.imread("ch08_images\\translate.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상 파일 읽기 오류")

M = np.array([[1,0,100],
            [0,1,100]], dtype = np.float32)

dst = cv2.warpAffine(image, M, (0, 0))

cv2.imshow("image", image)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()