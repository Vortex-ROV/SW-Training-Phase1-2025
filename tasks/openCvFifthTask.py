import cv2
import numpy as np 
circles = np.zeros((4,2),np.int_)
count=0
def points(event,x,y,flags,pram):
    global count
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[count] =x,y
        count+=1
        print(x,y)

img = cv2.imread("tasks\jhonsmith.jpg")
while True:
    if count==4:
        w,h = 250,350
        pt1 = np.float32([circles[0],circles[1],circles[2],circles[3]])
        pt2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
        matrix = cv2.getPerspectiveTransform(pt1,pt2)
        output =cv2.warpPerspective(img,matrix,(w,h))
        cv2.imshow("output",output)
        
    
    for x in range(0,4):
        cv2.circle(img,(circles[x][0],circles[x][1]),4,(0,255,0),cv2.FILLED)
    cv2.imshow("img",img)
    cv2.setMouseCallback("img", points)
    cv2.waitKey(1)
        