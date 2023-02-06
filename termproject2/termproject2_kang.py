'''강민규'''
import cv2 
import numpy as np

def preprocessing():
    image = cv2.imread("face.jpg",cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    if image is None:
        return None , None
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    return image , gray

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
image , gray = preprocessing()
if image is None: 
    raise Exception("영상 파일 읽기 에러")

glasses = cv2.imread("glasses.png", cv2.IMREAD_UNCHANGED)

if glasses is None: 
    raise Exception("영상 파일 읽기 에러")

def get_angle(eye_centers):
    pt0 , pt1 = eye_centers
    if pt0[0] > pt1[0]:pt0, pt1 = pt1, pt0

    dx , dy = np.subtract(pt1, pt0)
    angle = np.arctan2(dy, dx)*180/np.pi
    return angle

faces = face_cascade.detectMultiScale(gray, 1.1,2,0,(100,100))
results = []
cv2.imshow("image", image)
cv2.waitKey(0)
if faces.any():
    for f in faces:
        x, y, h, w= f
        face_image = image[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(face_image, 1.15,7,0, (25,20))

        glass = cv2.resize(glasses, (w, h))

        if len(eyes) ==2:
            eye_centers = [(ex+ew//2 , ey+eh //2) for ex, ey ,ew, eh in eyes]

            eye = np.mean(eye_centers, axis=0)

            angle = get_angle(eye_centers)

            M = cv2.getRotationMatrix2D((glass.shape[0]/2.0, glass.shape[1]/2.0), #회전 중심
                                angle, # 회전각도(양수 반시계방향, 음수 시계방향)
                                1) # 이미지 배율

            dst = cv2.warpAffine(glass, M, (glass.shape[1], glass.shape[0]))
            dst = cv2.flip(dst, 1)

            height, width = dst.shape[:2]
            x, y = eye - (width//2, height//2)
            M = np.float32([[1, 0, x], [0, 1, y]])
            dst = cv2.warpAffine(dst, M, (width,height))
            
            face_image[dst[:,:,3] != 0] = dst[dst[:,:,3] != 0]
            face_image = cv2.resize(face_image, (256, 256))
            results.append(face_image)
            # cv2.imshow("image", face_image)
            # cv2.waitKey(0)

        else: 
            print("눈 미검출")

else:
    print("얼굴 미검출")

img = results[0]
for i in results[1:]:
    img = cv2.hconcat([img, i])

cv2.imshow("image", img)
cv2.waitKey(0)