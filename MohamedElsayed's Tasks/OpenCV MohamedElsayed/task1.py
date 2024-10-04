import cv2
import numpy as np
myImg1 = cv2.imread('lena.jpg', 1)
myImg2 = cv2.imread('lena.jpg', 0)
myImg3 = cv2.cvtColor(myImg1, cv2.COLOR_BGR2HSV)
grayFrameBgr = cv2.cvtColor(myImg2, cv2.COLOR_GRAY2BGR)
myImg4 = cv2.cvtColor(grayFrameBgr, cv2.COLOR_BGR2HSV)


combined = np.hstack((myImg1, grayFrameBgr, myImg3,myImg4))

cv2.imshow('combined',combined)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()




