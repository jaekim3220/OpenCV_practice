'''그리기 함수'''
import numpy as np
import cv2
# # 1
# blue, green, red = (255,0,0),(0,255,0),(0,0,255)
# image = np.zeros((400,600,3),np.uint8)
# image[:]=(255,255,255)

# pt1, pt2 = (50,50), (250,350)
# pt3, pt4 = (400,150), (500,50)
# roi = (50,200,200,100)

# cv2.line(image,pt1,pt2,red)
# cv2.line(image,pt3,pt4,green,3,cv2.LINE_AA)

# cv2.rectangle(image,pt1,pt2,blue,3,cv2.LINE_4)
# cv2.rectangle(image,roi,red,3,cv2.LINE_8)
# cv2.rectangle(image,(400,200,100,100),green,cv2.FILLED)

# cv2.imshow("LINE&RECTANGLE", image)
# cv2.waitKey(0)

# # 2
# olive,violet,brown = (128,128,0),(221,160,221),(42,42,165)
# pt1,pt2 = (50,230), (50,310)

# image = np.zeros((350,500,3), np.uint8)
# image.fill(255)

# cv2.putText(image, 'SIMPLEX', (50,50),cv2.FONT_HERSHEY_SIMPLEX,2,brown)
# cv2.putText(image, 'DUPLEX', (50,130),cv2.FONT_HERSHEY_DUPLEX,3,olive)
# cv2.putText(image, 'TRIPLEX', pt1, cv2.FONT_HERSHEY_TRIPLEX,2,violet)
# fontFace = cv2.FONT_HERSHEY_PLAIN | cv2.FONT_ITALIC
# cv2.putText(image, 'ITALIC', pt2, fontFace, 4, violet)

# cv2.imshow('Put Text', image)
# cv2.waitKey(0)

# # 3
# orange,blue,cyan=(0,165,255), (255,0,0),(255,255,0)
# white, black = (255,255,255), (0,0,0)
# image = np.full((300,500,3), white, np.uint8)

# center = (image.shape[1]//2,image.shape[0]//2)
# pt1,pt2 = (300,50), (100,220)
# shade = (pt2[0]+2,pt2[1]+2)

# cv2.circle(image,center,100,blue)
# cv2.circle(image,pt1,50,orange,2)
# cv2.circle(image,pt2,70,cyan,-12)

# font = cv2.FONT_HERSHEY_COMPLEX
# cv2.putText(image,'center_blue', center, font,1.0,blue)
# cv2.putText(image,'pt1_orange', pt1, font,0.8,orange)
# cv2.putText(image,'pt2_cyan', shade, font,1.2,black,2)
# cv2.putText(image,'pt2_cyan', pt2, font,1.2,cyan,1)

# cv2.imshow('Draw Circles', image)
# cv2.waitKey(0)

# # 4
# orange,blue,white = (0,165,255),(255,0,0),(255,255,255)
# image = np.full((300,700,3),white,np.uint8)

# pt1, pt2 = (180,150), (550,150)
# size = (120,60)

# cv2.circle(image,pt1,1,0,2)
# cv2.circle(image,pt2,1,0,2)

# cv2.ellipse(image,pt1,size,0,0,360,blue,1)
# cv2.ellipse(image,pt2,size,90,0,360,blue,1)
# cv2.ellipse(image,pt1,size,0,30,270,orange,4)
# cv2.ellipse(image,pt2,size,90,-45,90,orange,4)

# cv2.imshow("문자열",image)
# cv2.waitKey()

# # 5
# def onMouse(event, x, y, flags, param):
#     global title, pt
#     if event == cv2.EVENT_LBUTTONDOWN:
#         if pt[0] < 0:
#             pt = (x,y)
#         else:
#             cv2.rectangle(image,pt,(x,y),(255,0,0),2)
#             cv2.imshow(title,image)
#             pt = (-1,-1)
#     elif event == cv2.EVENT_RBUTTONDOWN:
#         if pt[0] < 0:
#             pt = (x,y)
#         else:
#             dx,dy = pt[0]-x, pt[1]-y
#             radius = int(np.sqrt(dx*dx +dy*dy))
#             cv2.circle(image,pt,radius, (0,0,255),2)
#             cv2.imshow(title,image)
#             pt=(-1,-1)
# image=np.full((300,500,3),(255,255,255),np.uint8)

# pt=(-1,-1)
# title="Draw Event"
# cv2.imshow(title, image)
# cv2.setMouseCallback(title, onMouse)
# cv2.waitKey(0)

