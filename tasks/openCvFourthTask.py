import cv2
import numpy as np 
circles = []
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((x, y, 20))
cv2.namedWindow("Draw Circles")
cv2.setMouseCallback("Draw Circles", draw_circle)
while True:
    img = np.zeros((512, 512, 3), dtype="uint8")
    for (x, y, radius) in circles:
        cv2.circle(img, (x, y), radius, (0, 255, 0), -1)  
    
    cv2.imshow("Draw Circles", img)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('d') and circles:
        circles.pop()

    if key == ord('a'):
        circles.clear()

    if key == ord('q'):
        break
cv2.destroyAllWindows()