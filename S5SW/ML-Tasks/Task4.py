import cv2
import numpy as np

circles = []

def draw_circle(event, x, y, flags, param):
    global circles
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((x, y, 20))
    elif event == cv2.EVENT_RBUTTONDOWN:
        if circles:
            circles.pop()
    elif event == cv2.EVENT_MBUTTONDOWN:
        circles = []

canvas = np.zeros((500, 500, 3), dtype="uint8")
canvas[:,:,0]=255
canvas[:,:,1]=255
canvas[:,:,2]=255

cv2.namedWindow("Circles")
cv2.setMouseCallback("Circles", draw_circle)

while True:
    output_canvas = canvas.copy()

    for (x, y, radius) in circles:
        cv2.circle(output_canvas, (x, y), radius, (0, 0, 255), -1) 

    cv2.imshow("Circles", output_canvas)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
