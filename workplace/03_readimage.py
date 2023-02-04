import numpy as np
import cv2

# def print_matInfo(name, image):
#     if image.dtype == 'uint8':     mat_type = "CV_8U"
#     elif image.dtype == 'int8':    mat_type = "CV_8S"
#     elif image.dtype == 'uint16':  mat_type = "CV_16U"
#     elif image.dtype == 'int16':   mat_type = "CV_16S"
#     elif image.dtype == 'float32': mat_type = "CV_32F"
#     elif image.dtype == 'float64': mat_type = "CV_64F"
#     nchannel = 3 if image.ndim == 3 else 1

#     ## depth, channel 출력
#     print("%12s: depth(%s), channels(%s) -> mat_type(%sC%d)"
#           % (name, image.dtype, nchannel, mat_type,  nchannel))

# title1, title2 = 'gray2gray', 'gray2color'
# gray2gray = cv2.imread("mine1.jpg", cv2.IMREAD_GRAYSCALE)
# gray2color = cv2.imread("mine1.jpg", cv2.IMREAD_COLOR)

# if gray2gray is None or gray2color is None:
#     raise Exception("영상파일 읽기 에러")

# print("행렬 좌표(100,100) 화소값")
# print("%s %s" % (title1, gray2gray[100,100]))
# print("%s %s\n" % (title2, gray2color[100,100]))

# print_matInfo(title1, gray2gray)
# print_matInfo(title2, gray2color)

# cv2.imshow(title1, gray2gray)
# cv2.imshow(title2, gray2color)
# cv2.waitKey(0)


# image = cv2.imread("images/read_color.jpg", cv2.IMREAD_COLOR)
# if image is None:
#     raise Exception("영상파일 읽기 에러")

# params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 10)
# params_png = [cv2.IMWRITE_PNG_COMPRESSION, 9]

# # 행렬을 영상파일로 저장
# cv2.imwrite("images/write_test1.jpg", image)
# cv2.imwrite("images/write_test2.jpg", image, params_jpg)
# cv2.imwrite("images/write_test3.jpg", image, params_png)
# cv2.imwrite("images/write_test4.jpg", image)
# print("저장 완료")


# image8 = cv2.imread("images/read_color.jpg", cv2.IMREAD_COLOR)
# if image8 is None:
#     raise Exception("영상파일 읽기 에러")

# image16 = np.uint16(image8 * (65535/255))
# image32 = np.float32(image8 * (1/255))

# # 화소값 확인 - 관심 영역((10,10) 위치에서 2행, 3열) 출력
# print("image8 행렬의 일부\n %s\n" % image8[10:12, 10:13])
# print("image16 행렬의 일부\n %s\n" % image16[10:12, 10:13])
# print("image32 행렬의 일부\n %s\n" % image32[10:12, 10:13])

# cv2.imwrite("images/write_test_16.tif", image16)
# cv2.imwrite("images/write_test_32.tif", image32)

# cv2.imshow("image16", image16)
# cv2.imshow("image32", (image32*255).astype('uint8'))
# cv2.waitKey(0)


