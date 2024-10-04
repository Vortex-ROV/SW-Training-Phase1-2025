import cv2
import numpy as np

allPoints = []
image = cv2.imread("jhonsmith.jpg")

def selectEvent(event, x, y, flags, param):
    global allPoints
    if event == cv2.EVENT_LBUTTONDOWN:
        allPoints.append((x, y))
        cv2.circle(image, (x, y), 10, (255, 255, 0), -1)
        cv2.imshow('Image', image)
        
        if len(allPoints) == 4:
            warpCard()

def warpCard():
    global allPoints
    width, height = 300, 200
    point1 = np.float32(allPoints)
    point2 = np.float32([ [0,0] , [ width,0 ] , [width,height] , [0,height ]  ])
    matrix = cv2.getPerspectiveTransform(point1,point2)
    finalProduct = cv2.warpPerspective(image, matrix, (width,height))
    cv2.imshow("finalProduct",finalProduct)

cv2.imshow('Image', image)
cv2.setMouseCallback('Image', selectEvent)

cv2.waitKey(0)
cv2.destroyAllWindows()
