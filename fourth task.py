import cv2
import numpy as np

circles = []

def draw_circle(event, x, y, flags, param):
    global circles

    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((x, y))
    elif event == cv2.EVENT_RBUTTONDOWN:
        if circles:
            circles.pop()
    elif event == cv2.EVENT_MBUTTONDOWN:
        circles = []

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    img_copy = img.copy()
    
    for center in circles:
        cv2.circle(img_copy, center, 20, (79, 25, 100), -1)
    
    cv2.imshow('image', img_copy)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()