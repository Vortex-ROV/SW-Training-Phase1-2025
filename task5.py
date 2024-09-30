import cv2
import numpy as np

image = cv2.imread('E:/vortex peri/OpenCVExample/Tasks_Images2025/task_5/jhonsmith.jpg',1)

points =[]
def click_event (event ,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points)<4:
           cv2.circle(image,(x,y),3,(255,0,0),-1)
           points.append((x,y))
           cv2.imshow('image',image)


        if len(points)==4:
            
            trans_points = [[0,0],[400,0],[400,600],[0,600]]
            M = cv2.getPerspectiveTransform(np.float32(points),np.float32(trans_points))
            wraped_image = cv2.warpPerspective(image,M,(400,600))
            cv2.imshow('bird/view',wraped_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

cv2.imshow('image',image)    
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

