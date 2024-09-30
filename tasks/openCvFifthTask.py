import cv2
import numpy as np 
circles = np.zeros
def points(event,x,y,flags,pram):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
img = cv2.imread("tasks\jhonsmith.jpg")
cv2.imshow("img",img)
cv2.setMouseCallback("img", points)
cv2.waitKey(0)        