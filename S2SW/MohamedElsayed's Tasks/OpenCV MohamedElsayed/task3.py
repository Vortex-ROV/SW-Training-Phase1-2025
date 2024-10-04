import cv2
import numpy as np

width, height = 600, 600
grid_size = 50 

cordX, cordY = map(int, input().split())

image = np.ones((height, width, 3), np.uint8) * 255

for y in range(0, height, grid_size):
    cv2.line(image, (0, y), (width, y), (0, 0, 0), 1)

for x in range(0, width, grid_size):
    cv2.line(image, (x, 0), (x, height), (0, 0, 0), 1)
cv2.imshow("Grid", image)
image = cv2.circle(image, (cordX, cordY), 10, (0, 255, 0), -1)

cv2.imshow("Grid", image)
cv2.waitKey(0)
cv2.destroyAllWindows()