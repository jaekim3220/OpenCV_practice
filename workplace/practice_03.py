import numpy as np, cv2, math
from Common.interpolation import bilinear_value
from Common.utils import contain, ck_time

def rotate(img, degree): #원점 기준 회전 변환 함수
    dst = np.zeros(img.shape[:2], img.dtype) #목적 영상 생성
    radian = (degree/180) * np.pi #회전 각도
    sin, cos = np.sin(radian), np.cos(radian) #sin, cos 값 미리 계산

    for i in range(img.shape[0]): #목적 영상 순회 - 역방향 사상
        for j in range(img.shape[1]):
            y = -j*sin + i*cos
            x = j*cos + i*sin
            if contain((y,x), img.shape): #입력 변환 수식
                dst[i, j] = bilinear_value(img, [x, y])
    return dst

image = cv2.imread("ch08_images\\rotate.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상 파일 읽기 에러")

rotation_matrix = cv2.getRotationMatrix2D((100,100), 30, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, image.shape[1::-1])

cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)

'''
def rotate(img, degree, center):
    radian = (degree/180) * np.pi
    sin, cos = np.sin(radian), np.cos(radian)
    R = np.array([[cos, -sin], [sin, cos]])
    center = np.array(center).reshape(1, -1)
    img = cv2.warpAffine(img, R, img.shape[1::-1], flags=cv2.INTER_LINEAR, borderValue=0)
    return img

image = cv2.imread("ch08_images\\rotate.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("Error reading image file")

center = (100, 100)
dst = rotate(image, 30, center)

cv2.imshow("image", image)
cv2.imshow("rotated", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
