import numpy as np, cv2

# # 1 행렬
# m1 = np.full((3,6), 10, np.uint8) #단일채널 생성 및 초기화
# m2 = np.full((3,6), 50, np.uint8)
# m_mask = np.zeros(m1.shape, np.uint8) #마스크 생성
# m_mask[ :, 3: ] = 1 #관심 영역 지정 후 1을 할당

# m_add1 = cv2.add(m1,m2) #행렬 덧셈
# m_add2 = cv2.add(m1, m2, mask = m_mask) #관심 영역만 덧셈 수행

# # 행렬 나눗셈 수행
# m_div1 = cv2.divide(m1, m2)
# m1 = m1.astype(np.float32) #형변환 - 소수 부분 보존
# m2 = np.float32(m2)
# m_div2 = cv2.divide(m1, m2)

# titles =['m1', 'm1', 'm_mask', 'm_add1', 'm_add2', 'm_div1', 'm_div2']
# for title in titles:
#     print("[%s] = \n%s \n" % (title, eval(title)))

# # 2 지수, 로그, 제곱근
# x = np.array([1,2,3,5,10], np.float32) #리스트로 ndarray 객체 생성
# y = np.array([2,5,7,2,9]).astype("float32") #행렬 생성 후 실수형 변환

# mag = cv2.magnitude(x,y) #크기 계산
# ang = cv2.phase(x,y) #각도(방향) 계산
# p_mag, p_ang = cv2.cartToPolar(x,y) #극 좌표로 변환
# x2,y2 = cv2.polarToCart(p_mag, p_ang) #직교좌표로 변환

# print("[x] 형태 : %s 원소 : %s" % (x.shape, x)) #1차원 행렬
# print("[mag] 형태 : %s 원소 : %s" % (mag.shape, mag)) #2차원 열벡터

# print(">>열백터를 1행에 출력하는 방법")
# print("[m_mag] = %s" % mag.T) #행렬 전치
# print("[p_mag] = %s " % np.ravel(p_mag)) #ravel() 함수로 전개
# print("[p_ang] = %s " % np.ravel(p_ang))
# print("[x_mat2] = %s " % x2.flatten()) #2차원 행렬 전개
# print("[y_mat2] = %s " % y2.flatten())

# # 3 논리(비트) 연산 함수
# image1 = np.zeros((300,300), np.uint8) #300행, 300열 검은색 영상 생
# image2 = image1.copy()

# h, w = image1.shape[:2]
# cx, cy = w//2, h//2 
# cv2.circle(image1, (cx, cy), 100, 255,-1) #중심에 원 그리기
# cv2.rectangle(image2, (0,0,cx,h), 255,-1) #영상의 가로 절반

# image3 = cv2.bitwise_or(image1, image2) #원소 간 논리합
# image4 = cv2.bitwise_and(image1, image2) #원소 간 논리곱
# image5 = cv2.bitwise_xor(image1, image2) #원소 간 배타적 논리합
# image6 = cv2.bitwise_not(image1) #행렬 반전

# cv2.imshow("image1", image1);   cv2.imshow("image2", image2)
# cv2.imshow("bitwise_or", image3);   cv2.imshow("bitwise_and", image4)
# cv2.imshow("bitwise_xor", image5);  cv2.imshow("bitwise_not", image6)
# cv2.waitKey(0)

# # 4 
# image = cv2.imread("ch05_images\bit_test.jpg", cv2.IMREAD_COLOR)
# logo = cv2.imread("ch05_images\logo.jpg", cv2.IMREAD_COLOR)
# if image is None or logo is None:
#     raise Exception("영상 파일 읽기 오류")

# masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]
# masks = cv2.split(masks)

# fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])
# fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)
# bg_pass_mask = cv2.bitwise_not(fg_pass_mask)

# (H, W), (h, w) = image.shape[:2], logo.shape[:2]
# x,y = (W-w)//2, (H-h)//2
# roi = image[y:y+h, x:x+w]

# forground = cv2.bitwise_and(logo, logo, mask = fg_pass_mask)
# background = cv2.bitwise_and(roi, roi, mask = bg_pass_mask)

# dst = cv2.add(background, forground)
# image[y:y+h, x:x+w] = dst

# cv2.imshow('background', background);   cv2.imshow('forground', forground)
# cv2.imshow('dst', dst); cv2.imshow('image', image)
# cv2.waitKey()

