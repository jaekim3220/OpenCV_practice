'''조현근님'''
import cv2
import numpy as np
import pytesseract

TESSERACT_PATH = "C:\Program Files\Tesseract-OCR\\tesseract.exe"

imgpath='termproject1/namecard.jpg'  #이미지 파일 경로
win_name = "Image To Text"  #OpenCV 창 이름
img = cv2.imread(imgpath)   #이미지 읽어오기
pos_l = []

# print(img.shape)   # 1400, 1050
img = cv2.resize(img, (800, 600))
dst = np.zeros(img.shape)

#마우스 이벤트 처리 함수
def onMouse(event, x, y, flags, param):
    global img
    global pos_l

    if event == cv2.EVENT_LBUTTONDOWN:
        if len(pos_l) < 4:
            pos_l.append(np.array([x, y]))
            cv2.circle(img, (x, y), 4, (0, 255, 0), -1)
        cv2.imshow(win_name, img)


#이미치 처리 함수
def ImgProcessing():
    global pos_l
    global dst

    if len(pos_l) == 4:
        pts1 = np.float32(pos_l)
        pts2 = np.float32([(50, 50), (50, 500), (750, 50), (750, 500)])

    perspect_mat = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, perspect_mat, img.shape[1::-1], cv2.INTER_CUBIC)
    
    return 0


#OCR 함수
def GetOCR():
    #이미지 불러오기
    # global img
    global dst

    #OCR모델 불러오기
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

    #OCR모델로 글자 추출
    text = pytesseract.image_to_string(dst, lang='kor+eng')
        
    return text


cv2.imshow(win_name, img)   #이미지 출력
cv2.setMouseCallback(win_name, onMouse)

cv2.waitKey(0)              #입력 대기

if len(pos_l) == 4:
    ImgProcessing()
    cv2.imshow("dst", dst)

cv2.waitKey(0)              #입력 대기

dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
cv2.imshow("dst", dst)
cv2.waitKey(0)

text = GetOCR()             #OCR함수로 텍스트 추출
print(text)                 #텍스트 출력
cv2.destroyAllWindows()
