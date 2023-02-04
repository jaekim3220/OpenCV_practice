import numpy as np, cv2, imutils

face_cascade = cv2.CascadeClassifier('termproject2\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('termproject2\haarcascade_eye.xml')

#얼굴이 포함된 이미지 불러오기
img = cv2.imread('termproject2\\faceimage.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Haar cascades 사용해 얼굴 인식
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Iterate over the faces detected
for (x,y,w,h) in faces:
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

    # 얼굴에서 눈 부분 인식
    eyes = eye_cascade.detectMultiScale(roi_gray)

    # 눈 위치를 통해 얼굴 각도 변화 크기 확인
    if len(eyes) >= 2:
        eye1 = eyes[0]
        eye2 = eyes[1]
        dy = eye2[1] - eye1[1]
        dx = eye2[0] + eye2[2]/2 - (eye1[0] + eye1[2]/2)
        angle = np.degrees(np.arctan2(dy, dx))

        # 안경 이미지 준비
        glasses = cv2.imread('termproject2\sunglasses1.png')
        glasses = cv2.resize(glasses, (w, h), interpolation = cv2.INTER_CUBIC)

        # 눈 중심, 안경 중심 계산
        x1 = x + eye1[0] + eye1[2]/2 - glasses.shape[1]/2
        y1 = y + eye1[1] + eye1[3]/2 - glasses.shape[0]/2
        x2 = x + eye2[0] + eye2[2]/2 - glasses.shape[1]/2
        y2 = y + eye2[1] + eye2[3]/2 - glasses.shape[0]/2

        # 눈 위치에 안경 이미지 반영
        roi_color[:glasses.shape[0], :glasses.shape[1]] = glasses
        img[np.int32(y1):np.int32(y1+glasses.shape[0]), np.int32(x1):np.int32(x1+glasses.shape[1])] = roi_color
        img[np.int32(y2):np.int32(y2+glasses.shape[0]), np.int32(x2):np.int32(x2+glasses.shape[1])] = roi_color


# 최종 결과물
cv2.imshow('Sunglasses Filter', img)
cv2.waitKey(0)
cv2.destroyAllWindows()