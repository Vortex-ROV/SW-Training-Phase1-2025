import cv2
import numpy as np

# Initialize the image and list to store circles
img = np.zeros((512, 512, 3), dtype=np.uint8)
circles = []

def draw_circles():
    img[:] = 0  # Clear the image
    # Draw all circles from the list
    for center, radius, color in circles:
        cv2.circle(img, center, radius, color, 2)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Add a new circle on left click
        center = (x, y)
        radius = 20
        color = (255, 255, 0)
        circles.append((center, radius, color))
        draw_circles()        
        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        # Remove the last circle on right click
        if circles:
            circles.pop()
            draw_circles()
            cv2.imshow('image', img)

# Show the image and set the mouse callback
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)

# Main loop to handle key events
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):  # Clear all circles with 'c' key
        circles.clear()
        draw_circles()
        cv2.imshow('image', img)
    elif key == ord('q'):  # Press 'q' to exit
        break

cv2.destroyAllWindows()
