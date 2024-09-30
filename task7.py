import cv2
import numpy as np

img = cv2.imread('E:/vortex peri/OpenCVExample/Tasks_Images2025/task_7/shapes_sizes.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('imgary',imgray)
_, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)


contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contour_area = [(cnt, cv2.contourArea(cnt)) for cnt in contours if cv2.contourArea(cnt) > 0]

sorted_contours = sorted(contour_area, key=lambda x: x[1], reverse=True)


# Print  areas in order
for cnt, area in sorted_contours:
    print(f'Contour Area: {area:.2f}')

cv2.waitKey(0)
cv2.destroyAllWindows()
