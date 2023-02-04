import numpy as np, cv2, imutils

face_cascade = cv2.CascadeClassifier('termproject2\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('termproject2\haarcascade_eye.xml')
glasses = cv2.imread("termproject2\sunglasses1.png", -1)

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            roi_eyes = roi_gray[ey:ey + eh, ex:ex + ew]
            glasses_resized = cv2.resize(glasses.copy(), (ew, eh), interpolation = cv2.INTER_CUBIC)
            transparent_region = glasses_resized[:, :, 3] != 0
            roi_color[ey:ey + eh, ex:ex + ew][transparent_region] = glasses_resized[:, :, :3][transparent_region]

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()