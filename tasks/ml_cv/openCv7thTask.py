import cv2
import numpy as np

img = cv2.imread('tasks\ml_cv\shapes_sizes.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresholded = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)
edges = cv2.Canny(gray, 50, 150)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)
if len(contours) > 0:
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    print(f"Number of contours found: {len(contours)}")
    for i, contour in enumerate(contours):
        color = (0,255,0)
        cv2.drawContours(img, [contour], -1, color, 3)
        area = cv2.contourArea(contour)
        print(f"Contour {i+1} area: {area}")
    cv2.imshow('Contours', img)
else:
    print("No contours found.")

cv2.waitKey(0)
cv2.destroyAllWindows()
