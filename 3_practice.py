import numpy as np
import cv2
# # 연습문제_1
# image = np.zeros((300,400,3),np.uint8)
# image[:] = (255,255,255)
# pt1,pt2 = (50,130),(200,300)

# cv2.line(image,pt1,(100,200))
# cv2.line(image,pt2,(100,100,100))
# cv2.rectangle(image,pt1,pt2,(255,0,255))
# cv2.rectangle(image,pt1,pt2,(255,0,255))
# cv2.rectangle(image,pt1,pt2,(0,0,255))

# title = "Line&Rectangle"
# cv2.namedWindow(title)
# cv2.imshow(title,image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # 연습문제_2
# def onMouse(event, x,y,flasgs,param):
#     global title
#     pt = (x,y)
#     if event == cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(image,pt,5,100,1)
#         cv2.imshow(title,image)
#     elif event == cv2.EVENT_RBUTTONDOWN:
#         pt2 = (pt[0]+30, pt[1]+30)
#         cv2.rectangle(image, pt, pt+(30,30),100,2)
#         cv2.imshow(title,image)

# image = np.ones((300,300),np.uint8)*255
# title = "Draw Event"

# cv2.namedWindow(title)
# cv2.imshow(title,image)
# cv2.setMouseCallback(title, onMouse)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# def onMouse(event, x,y,flasgs,param):
#     global title
#     pt = (x,y)
#     if event == cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(image,pt,5,(100,100,100),1)
#         cv2.imshow(title,image)
#     elif event == cv2.EVENT_RBUTTONDOWN:
#         pt2 = (pt[0]+30, pt[1]+30)
#         cv2.rectangle(image, pt, pt2,(100,100,100),2)
#         cv2.imshow(title,image)

# image = np.ones((300,300),np.uint8)*255
# title = "Draw Event"

# cv2.namedWindow(title)
# cv2.imshow(title,image)
# cv2.setMouseCallback(title, onMouse)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # 연습문제_3
# def onMouse(event,x,y,flags,param):
#     global title,pt
#     if event == cv2.EVENT_LBUTTONDOWN:
#         if pt[0]<0:
#             pt = (x,y)
#         else:
#             cv2.rectangle(image, pt,(x,y),(255,0,0),2)
#             cv2.imshow(title,image)
#             pt=(-1,-1)
#     elif event == cv2.EVENT_RBUTTONDOWN:
#         if pt[0]<0:
#             pt=(x,y)
#         else:
#             dx,dy=pt[0]-x, pt[1]-y
#             radius = int(np.sqrt(dx*dx+dy*dy))
#             cv2.circle(image,pt,radius,(0,0,255),2)
#             cv2.imshow(title,image)
#             pt=(-1,-1)
# image=np.full((300,500,3),(255,255,255),np.uint8)

# pt = (-1,-1)
# title = "Draw Event"
# cv2.imshow(title, image)
# cv2.setMouseCallback(title, onMouse)
# cv2.waitKey(0)

# def onMouse(event,x,y,flags,param):
#     global title,pt
#     if event == cv2.EVENT_LBUTTONDOWN:
#         if pt[0]<0:
#             pt = (x,y)
#         else:
#             cv2.rectangle(image, pt,(x,y),(255,0,0),2)
#             cv2.imshow(title,image)
#             pt=(-1,-1)
#     elif event == cv2.EVENT_RBUTTONDOWN:
#         if pt[0]<0:
#             pt=(x,y)
#         else:
#             dx,dy=pt[0]-x, pt[1]-y
#             radius = int(np.sqrt(dx*dx+dy*dy))
#             cv2.circle(image,pt,radius,(0,0,255),2)
#             cv2.imshow(title,image)
#             pt=(-1,-1)
#     elif event == cv2.EVENT_MBUTTONDOWN:
#         if pt[0]<0:
#             pt=(x,y)
#         else:
#             cv2.ellipse(image,pt,(x,y),0,0,360,(0,255,0),2)
#             cv2.imshow(title,image)
#             pt=(-1,-1)

# image=np.full((300,500,3),(255,255,255),np.uint8)

# pt = (-1,-1)
# title = "Draw Event"
# cv2.namedWindow(title)
# cv2.imshow(title, image)
# cv2.setMouseCallback(title, onMouse)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # 연습문제_4
# def onMouse(event,x,y,flags,param):
#     global pt
#     if event == cv2.EVENT_LBUTTONDOWN:
#         pt = (x,y)
#         cv2.rectangle(image, (pt[0]-15, pt[1]-15), (pt[0]+15, pt[1]+15), (255,0,0), 2)
#     elif event == cv2.EVENT_RBUTTONDOWN:
#         pt = (x,y)
#         cv2.circle(image, pt, 20, (0,0,255), 2)

# image=np.full((300,500,3),(255,255,255),np.uint8)
# pt = (-1,-1)
# title = "Draw Event"
# cv2.namedWindow(title)
# cv2.setMouseCallback(title, onMouse)

# while True:
#     cv2.imshow(title, image)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break

# cv2.destroyAllWindows()

# # 연습문제_5
def onMouse(event,x,y,flags,param):
    global pt, line_thickness, circle_radius
    if event == cv2.EVENT_LBUTTONDOWN:
        pt = (x,y)
        cv2.rectangle(image, (pt[0]-15, pt[1]-15), \
            (pt[0]+15, pt[1]+15), (255,0,0), line_thickness)
    elif event == cv2.EVENT_RBUTTONDOWN:
        pt = (x,y)
        cv2.circle(image, pt, circle_radius, \
            (0,0,255), line_thickness)

def onLineThicknessTrackbar(value):
    global line_thickness
    line_thickness = value

def onCircleRadiusTrackbar(value):
    global circle_radius
    circle_radius = value

image = np.full((300, 500, 3), (255, 255, 255), np.uint8)
pt = (-1, -1)
line_thickness = 1
circle_radius = 20
title = "Draw Event"
cv2.namedWindow(title)
cv2.setMouseCallback(title, onMouse)
cv2.createTrackbar("Line Thickness", title, \
    1, 10, onLineThicknessTrackbar)
cv2.createTrackbar("Circle Radius", title, \
    1, 50, onCircleRadiusTrackbar)

while True:
    cv2.imshow(title, image)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()