import numpy as np, cv2

# # 1
# image1 = cv2.imread("ch05_images\\abs_test1.jpg", cv2.IMREAD_GRAYSCALE)
# image2 = cv2.imread("ch05_images\\abs_test2.jpg", cv2.IMREAD_GRAYSCALE)
# if image1 is None or image2 is None:
#     raise Exception("영상 파일 읽기 오류")

# dif_img1 = cv2.subtract(image1, image2)
# dif_img2 = cv2.subtract(np.int16(image1), np.int16(image2))
# abs_dif1 = np.absolute(dif_img2).astype('uint8')
# abs_dif2 = cv2.absdiff(image1, image2)

# x, y, w, h = 100, 150, 7, 3
# print("[dif_img1(roi) uint8] = \n%s\n" % dif_img1[y:y+h, x:x+w])
# print("[dif_img2(roi) int16] = \n%s\n" % dif_img2[y:y+h, x:x+w])
# print("[abs_dif1(roi)] = \n%s\n" % abs_dif1[y:y+h, x:x+w])
# print("[abs_dif2(roi)] = \n%s\n" % abs_dif2[y:y+h, x:x+w])

# titles = ['image1', 'image2', 'dif_img1', 'abs_dif1', 'abs_dif2']
# for title in titles:
#     cv2.imshow(title, eval(title))
# cv2.waitKey(0)

# # 2
# data = [10, 200, 5 , 7 ,  9,
#         15, 35 , 60, 80, 170,
#         100, 2 , 55, 37, 70]
# m1 = np.reshape(data, (3, 5))   # 리스트를 행태변환하여 행렬 생성
# m2 = np.full((3, 5), 50)              # 원소값 50인 행렬 생성

# m_min = cv2.min(m1, 30)                  # 두 행렬 원소 간 최솟값을 행렬로 저장
# m_max = cv2.max(m1, m2)                  # 두 행렬 최댓값 계산

# ## 행렬의 최솟값/최댓값과 그 좌표들을 반환
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(m1)

# print("[m1] = \n%s\n" % m1)
# print("[m_min] = \n%s\n" % m_min)
# print("[m_max] = \n%s\n" % m_max)

# # min_loc와 max_loc 좌표는 (y, x)이므로 행렬의 좌표 위차와 반대임
# print("m1 행렬 최솟값 좌표 %s, 최솟값: %d" %(min_loc, min_val))
# print("m1 행렬 최댓값 좌표 %s, 최댓값: %d" %(max_loc, max_val))

# # 3
# image = cv2.imread("ch05_images\minMax.jpg", cv2.IMREAD_GRAYSCALE)
# if image is None:
#     raise Exception("영상 파일 읽기 오류 발생")

# (min_val, max_val, _, _) = cv2.minMaxLoc(image)  # 최솟값과 최댓값 가져오기

# ratio = 255/(max_val - min_val)
# dst = np.round((image - min_val) * ratio).astype('uint8')
# (min_dst, max_dst, _, _) = cv2.minMaxLoc(dst)

# print("원본 영상 최솟값= %d , 최댓값= %d" % (min_val, max_val))
# print("수정 영상 최솟값= %d , 최댓값= %d" % (min_dst, max_dst))
# cv2.imshow("image", image)
# cv2.imshow("dst"  , dst)
# cv2.waitKey(0)

# # 4

# image = cv2.imread("ch05_images/sum_test.jpg", cv2.IMREAD_GRAYSCALE)
# if image is None:
#     raise Exception("영상 파일 읽기 오류 발생")
    
# mask = np.zeros(image.shape[:2], np.uint8)
# mask[60:160, 20:120] = 255                      # 관심영역을 지정한 후, 255를 할당

# sum_value   = cv2.sumElems(image)               # 채널별 합 구하기
# mean_value1 = cv2.mean(image)                   # 결과 튜플로 반환
# mean_value2 = cv2.mean(image, mask)

# print('sum_value 자료형:', type(sum_value), type(sum_value[0]))
# print("[sum_value] = ", sum_value)
# print("[mean_value1] = ", mean_value1)
# print("[mean_value2] = ", mean_value2)
# print()

# # 5
# theta = 20*np.pi/180
# rot_mat = np.array(
#     [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]], np.float32
# )

# pts1 = np.array(
#     [(250,30), (400,70), (350, 250), (150,200)], np.float32
# )
# pts2 = cv2.gemm(pts1, rot_mat, 1, None, 1, flags=cv2.GEMM_2_T)

# for i, (pt1, pt2) in enumerate(zip(pts1, pts2)):
#     print("pts1[%d] = %s, pts2[%d] = %s" %(i, pt1, i, pt2))

# image = np.full((400, 500, 3), 255, np.uint8)
# cv2.polylines(image, [np.int32(pts1)], True, (0, 255, 0), 2)
# cv2.polylines(image, [np.int32(pts2)], True, (255, 0, 0), 3)
# cv2.imshow('image', image)
# cv2.waitKey(0)
