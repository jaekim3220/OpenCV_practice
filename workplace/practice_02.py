import numpy as np, cv2

# # 연습 문제 1
# image = cv2.imread("ch05_images\color.jpg", cv2.IMREAD_COLOR)
# if image is None:
#     raise Exception("영상 파일 읽기 오류")

# mask = np.zeros(image.shape[:2], np.uint8)
# center = (190, 170)

# mask_roi = cv2.ellipse(mask, center, (40, 80), 0, 0, 360, 255, -1)

# result = cv2.bitwise_and(image, image, mask=mask_roi)

# cv2.imshow("Only Ellipses", result)
# cv2.waitKey()
# cv2.destroyAllWindows()

# # 연습 문제 2


# # 연습 문제 3


# # 연습 문제 4
image1 = cv2.imread("ch06_images/add1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("ch06_images/add2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None:
    raise Exception("영상파일 읽기 오류")

def adjust_alpha_beta(val):
    alpha = cv2.getTrackbarPos("Alpha", "dst") / 100.0
    beta = cv2.getTrackbarPos("Beta", "dst") / 100.0
    add_img = cv2.addWeighted(image1, alpha, image2, beta, 0)
    res = np.hstack((image1, add_img, image2))
    cv2.imshow("dst", res)
    
cv2.namedWindow("dst", cv2.WINDOW_NORMAL)
cv2.resizeWindow("dst", 720, 400)
cv2.createTrackbar("Alpha", "dst", 60, 100, adjust_alpha_beta)
cv2.createTrackbar("Beta", "dst", 70, 100, adjust_alpha_beta)
adjust_alpha_beta(0)
cv2.waitKey(0)