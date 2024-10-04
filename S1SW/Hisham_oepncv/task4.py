import cv2
import numpy as np


circles = []

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        
        circles.append((x, y, 20))  


cv2.namedWindow('Draw Circles')
cv2.setMouseCallback('Draw Circles', draw_circle)

# Main loop
while True:

    canvas = 255 * np.ones((600, 800, 3), dtype=np.uint8)

    for (x, y, radius) in circles:
        cv2.circle(canvas, (x, y), radius, (0, 0, 255), -1)  

    cv2.imshow('Draw Circles', canvas)

    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # Press Q to quit
        break
    elif key == ord('d') and circles:  # Press D to delete the last drawn circle
        circles.pop()
        print("Deleted the last drawn circle.")
    elif key == ord('a'):  # Press A to delete all circles
        circles.clear()
        print("Deleted all circles.")


cv2.destroyAllWindows()
