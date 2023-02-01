# import cv2
# import numpy as np
# print(cv2.__version__)

# a = np.array([1.111,2.222,3.333,4.444,5.555,6.666,7.777,8.888,9.999,10.123])
# print(round(np.sum(a),2))
# print(round(np.mean(a),2))
# print(f"{np.mean(a):.2f}")

# import random
# from collections import Counter
# random_num = [random.randint(0,50) for i in range(500)]
# counter = Counter(random_num)
# most_common = counter.most_common(3)
# print(most_common)

# import numpy as np
# import cv2
# image = np.zeros((200,300), np.uint8)
# # image[:] = 200
# image.fill(255)
# # title1,title2 = 'positon1', 'positon2'
# title1,title2 = 'autosize', 'normal'
# cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
# cv2.namedWindow(title2, cv2.WINDOW_NORMAL)
# cv2.imshow(title1, image)
# cv2.imshow(title2, image)
# cv2.resizeWindow(title1, 400,300)
# cv2.resizeWindow(title2, 400,300)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # keyboard event
# import numpy as np
# import cv2
# # switch case문을 사전으로 구현
# switch_case = {
#     ord('a') : "a키 입력",
#     ord('b') : "b키 입력",
#     0x41 : "A키 입력",
#     int('0x42', 16) : "B키 입력",
#     2424832 : "왼쪽 화살표키 입력",
#     2490368 : "윗쪽 화살표키 입력",
#     2621440 : "아래쪽 화살표키 입력"
# }
# image = np.ones((200, 300), np.float64)
# cv2.namedWindow('Keyboard Event')
# cv2.imshow('Keyboard Event', image)
# while True:
#     key = cv2.waitKeyEx(100)
#     if key == 27: 
#         break
#     try:
#         result = switch_case[key]
#         print(result)
#     except KeyError:
#         result = -1
# cv2.destroyAllWindows()

# # mouse event
# import numpy as np
# import cv2
# def onMouse(event, x,y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print("마우스 왼쪽 버튼 누르기")
#     elif event == cv2.EVENT_RBUTTONDOWN:
#         print("마우스 오른쪽 버튼 누르기")
#     elif event == cv2.EVENT_RBUTTONUP:
#         print("마우스 오른쪽 버튼 떼기")
#     elif event == cv2.EVENT_LBUTTONDBLCLK:
#         print("마우스 왼쪽 버튼 떼기")
# image = np.full((200,300), 255, np.uint8)
# title1, title2 = "ME1", "ME2"
# cv2.imshow(title1, image)
# cv2.imshow(title2, image)
# cv2.setMouseCallback('ME1', onMouse)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# trackbar
# import numpy as np
# import cv2
# def onChange(val):
#     global image, title
#     add_val = val - int(image[0][0])
# #     print("추가 화소값 : ", add_val)
#     image[:] = image + add_val
#     cv2.imshow(title, image)
# image = np.zeros((300,500), np.uint8)
# title = 'Trackbar Event'
# cv2.imshow(title, image)
# cv2.createTrackbar('Brightness', title, image[0][0],255,onChange)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# trackbar_2
# import numpy as np
# import cv2
# def onChange(value):
#     global image, title
#     add_value = value - int(image[0][0])
#     image[:] = image + add_value
#     cv2.imshow(title, image)
# def onMouse(event, x, y, flags, param):
#     global image, bar_name
#     if event == cv2.EVENT_RBUTTONDOWN:
#         print(image[0][0])
#         if(image[0][0]<246):
#             image[:] = image +10
#             cv2.setTrackbarPos(bar_name, title, image[0][0])
#             cv2.imshow(title, image)
#     elif event == cv2.EVENT_LBUTTONDOWN:
#         if(image[0][0]>=10):
#             image[:] = image-10
#             cv2.setTrackbarPos(bar_name, title, image[0][0])
#             cv2.imshow(title, image)
# image = np.zeros((300,500), np.uint8)
# title = 'Trackbar & Mouse Event'
# bar_name = "Brightness"
# cv2.imshow(title, image)
# cv2.createTrackbar(bar_name, title, image[0][0],255,onChange)
# cv2.setMouseCallback(title,onMouse)
# cv2.waitKey(0)
# cv2.destroyAllWindows()