'''신정열'''
import cv2, numpy as np
from pathlib import Path
import math
import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt
# image = cv2.imread('face.jpg')
# plt.imshow(image)
# plt.show()

glass = cv2.imread('glasses.jpg')

def combine(face, pos, size, degree, glass=glass):
    w, h = size
    h //= 2
    x, y = pos
    degree = 360 - degree
    glass = cv2.resize(glass, (w, h))
    mtx = cv2.getRotationMatrix2D((w//2, h//2), degree, 1)
    glass = cv2.warpAffine(glass, mtx, (w, h), borderValue=(255, 255, 255))
    # bgrLower = np.array([0, 0, 0])  # 추출할 색의 하한(BGR)
    # bgrUpper = np.array([1, 1, 1])  # 추출할 색의 상한(BGR)
    # img_mask = cv2.inRange(glass, bgrLower, bgrUpper)  # BGR로 부터 마스크를 작성
    # glass[img_mask!=255] = (255, 255, 255)
    # glass = cv2.bitwise_and(glass, glass, mask=img_mask)

    mask = cv2.cvtColor(glass, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(mask, 240, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    roi = image[y - h//2 : y - h//2 + h, x - w//2 : x - w//2 + w]
    masked_glass = cv2.bitwise_and(glass, glass, mask=mask_inv)
    print(roi.shape, mask.shape)
    masked_face = cv2.bitwise_and(roi, roi, mask=mask)
    added = masked_glass + masked_face
    image[y - h//2 : y - h//2 + h, x - w//2 : x - w//2 + w] = added
    return image


def preprocessing(img_dir='./samples/face.jpg'):  # 검출 전처리
    image = cv2.imread(img_dir)
    print(image is None)
    if image is None: return None, None
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 명암도 영상 변환
    gray = cv2.equalizeHist(gray)  # 히스토그램 평활화
    return image, gray

xml_dir = Path('data/haarcascades')
face_cascade = cv2.CascadeClassifier(str(xml_dir / "haarcascade_frontalface_alt2.xml"))  # 정면 검출기
eye_cascade = cv2.CascadeClassifier(str(xml_dir / "haarcascade_eye.xml"))  # 눈 검출기
image, gray = preprocessing()  # 전처리
if image is None: raise Exception("영상 파일 읽기 에러")

faces = face_cascade.detectMultiScale(gray, 1.1, 2, 0, (100, 100));  # 얼굴 검출
if faces.any():
    for face in faces:
        x, y, w, h = face
        face_image = image[y:y + h, x:x + w]  # 얼굴 영역 영상 가져오기
        eyes = eye_cascade.detectMultiScale(face_image, 1.15, 7, 0, (25, 20))  # 눈 검출 수행
        center_pos = [0, 0]
        x_lst = []
        y_lst = []
        if len(eyes) == 2:  # 눈 사각형이 검출되면
            for ex, ey, ew, eh in eyes:
                center = (x + ex + ew // 2, y + ey + eh // 2)
                x_lst += [center[0]]
                y_lst += [center[1]]
                center_pos[0] += center[0]
                center_pos[1] += center[1]
                cv2.circle(image, center, 10, (0, 255, 0), 2)  # 눈 중심에 원 그리기
        else:
            print("눈 미검출")
        center_pos[0] //= 2
        center_pos[1] //= 2
        deg = math.atan2(abs(y_lst[0]-y_lst[1]), abs(x_lst[0]-x_lst[1])) * 180 / 3.14
        image = combine(image, center_pos, (int(w), int(h)), deg)

        cv2.rectangle(image, face, (255, 0, 0), 2)  # 얼굴 검출 사각형 그리기
        # cv2.imshow("image", image)


cv2.imshow('result', image)
cv2.waitKey(0)