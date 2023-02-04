import numpy as np, cv2, math
from Common.interpolation import bilinear_value
from Common.utils import contain, ck_time

# def rotate(img, degree): #원점 기준 회전 변환 함수
#     dst = np.zeros(img.shape[:2], img.dtype) #목적 영상 생성
#     radian = (degree/180) * np.pi #회전 각도
#     sin, cos = np.sin(radian), np.cos(radian) #sin, cos 값 미리 계산

#     for i in range(img.shape[0]): #목적 영상 순회 - 역방향 사상
#         for j in range(img.shape[1]):
#             y = -j*sin + i*cos
#             x = j*cos + i*sin
#             if contain((y,x), img.shape): #입력 변환 수식
#                 dst[i, j] = bilinear_value(img, [x, y])
#     return dst

# def rotate_pt(img, degree, pt): #pt 기준 회전 변환 함수
#     dst = np.zeros(img.shape[:2], img.dtype) #목적 영상 생성
#     radian = (degree/180) * np.pi #회전 각도
#     sin, cos = math.sin(radian), math.cos(radian) #sin, cos 값 미리 계산
#     #sin, cos = np.sin(radian), np.cos(radian) #으로 대체 가능

#     for i in range(img.shape[0]): 
#         for j in range(img.shape[1]):
#             jj, ii = np.subtract((j, i), pt) #중심 좌표로 평행이동
#             y = -jj * sin + ii * cos #회전 변환 수식
#             x = jj*cos + ii*sin 
#             x, y = np.add((x,y), pt) #중심 좌표로 평행 이동
#             if contain((y,x), img.shape): #입력 영상 범위 확인
#                 dst[i, j] = bilinear_value(img, (x,y)) #화소값 양선형 보간
#     return dst

# image = cv2.imread("ch08_images\\rotate.jpg", cv2.IMREAD_GRAYSCALE)
# if image is None:
#     raise Exception("영상 파일 읽기 에러")

# center = np.divmod(image.shape[::-1], 2)[0] #영상 크기로 중심 좌표 계산
# dst1 = rotate(image, 20) #원점 기준 회전 변홛
# dst2 = rotate_pt(image, 20, center) #center 기준 회전 변환

# cv2.imshow("image", image)
# cv2.imshow("dst1 : rotated on (0,0)", dst1)
# cv2.imshow("dst2 : rotated on center point", dst2)
# cv2.waitKey(0)

# # 8.6 행렬 연산을 통한 기하학 변환-어파인 변환
# image = cv2.imread("ch08_images\\affine.jpg", cv2.IMREAD_GRAYSCALE)
# if image is None:
#     raise Exception("영상 파일 읽기 에러")

# center = (200,200) #회전 변환 기준 좌표
# angle, scale = 30, 1 #회전 각도, 크기 지정 - 크기 변경은 안 함
# size = image.shape[::-1] #영상 크기는 행렬 형태의 역순

# #원본 좌표, 지정 좌표를 통한 회전 
# pt1 = np.array([(30,70), (20,240), (300,110)], np.float32) #변환 전 3개 좌표 지정
# pt2 = np.array([(120,20), (10,180), (280,260)], np.float32) #변환 후 3개 좌표 지정

# aff_mat = cv2.getAffineTransform(pt1, pt2) #3개 좌표 쌍으로 어파인 행렬 생성
# rot_mat = cv2.getRotationMatrix2D(center, angle, scale) #회전 변환을 위한 어파인 행렬

# dst3 = cv2.warpAffine(image, aff_mat, size, cv2.INTER_LINEAR)
# dst4 = cv2.warpAffine(image, rot_mat, size, cv2.INTER_LINEAR)

# image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
# dst3 = cv2.cvtColor(dst3, cv2.COLOR_GRAY2BGR)

# for i in range(len(pt1)):
#     cv2.circle(image, tuple(pt1[i].astype(int)), 3, (0,0,255), 2)
#     cv2.circle(dst3, tuple(pt2[i].astype(int)), 3, (0,0,255), 2)

# cv2.imshow("image", image)
# cv2.imshow("dst3_OpenCV_affine", dst3)
# cv2.imshow("dst4_OpenCV_affine_rotate", dst4)
# cv2.waitKey(0)

# # 8.7 원근 투시(투영) 변환
image = cv2.imread("ch08_images\perspective.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상 파일 읽기 에러")

pt1 = np.array([(80,40), (315,133), (75,300), (335,300)], np.float32) #변환 전 4개 좌표 지정
pt2 = np.array([(50,60), (340,60), (50,320), (340,320)], np.float32) #변환 후 4개 좌표 지정

perspect_mat = cv2.getPerspectiveTransform(pt1, pt2) #.astype('float32')

dst = cv2.warpPerspective(image, perspect_mat, image.shape[1::-1], cv2.INTER_CUBIC)

print("[perspect_mat] = \n%s\n" % perspect_mat)

cv2.imshow("image", image)
cv2.imshow("dst_perspective", dst)
cv2.waitKey(0)