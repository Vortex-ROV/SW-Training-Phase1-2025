import cv2
import numpy as np

circles = []

def draw_circle(event, x, y, flags, param):
    global circles
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((x, y, 30))
        update_image()

def update_image():
    global image
    image = np.ones((600, 600, 3), np.uint8) * 255
    for circle in circles:
        cv2.circle(image, (circle[0], circle[1]), circle[2], (0, 255, 0), -1)
    cv2.imshow('Draw Circles', image)

def delete_circle():
    if circles:
        circles.pop() 
        update_image()
    else:
        print("No circles to delete.")

def delete_all_circles():
    global circles
    if circles:
        circles = [] 
        update_image()
    else:
        print("No circles to delete.")


image = np.ones((600, 600, 3), np.uint8) * 255

cv2.imshow('Draw Circles', image)

cv2.setMouseCallback('Draw Circles', draw_circle)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  
        break
    elif key == ord('d'): 
        delete_circle()
    elif key == ord('a'):  
        delete_all_circles()

cv2.destroyAllWindows()