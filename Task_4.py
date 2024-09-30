import cv2
import numpy as np
import random

# List to store the circle parameters (center, radius, and color)
circles = []


# Mouse callback function to draw circles
def draw_circle(event, x, y, flags, param):
    global circles
    if event == cv2.EVENT_LBUTTONDOWN:
        # When left mouse button is pressed, add a circle at the click location
        radius = 30  # Fixed radius for the circle
        # Generate a random color (RGB format)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        circles.append((x, y, radius, color))


# Initialize window and set mouse
cv2.namedWindow("Circle Drawer")
cv2.setMouseCallback("Circle Drawer", draw_circle)

while True:
    # Create a blank image to draw circles on
    img = 255 * np.ones((500, 500, 3), dtype=np.uint8)

    # Draw all the circles from the list
    for (x, y, radius, color) in circles:
        cv2.circle(img, (x, y), radius, color, 2)  # 2 is the thickness of the circle's edge

    # Show the image with the drawn circles
    cv2.imshow("Circle Drawer", img)

    # Handle keypresses
    key = cv2.waitKey(1) & 0xFF

    # Press 'q' to quit the program
    if key == ord('q'):
        break
    # 'd' to delete the last drawn circle
    elif key == ord('d') and circles:
        circles.pop()
    # Press 'a' to delete all circles
    elif key == ord('a'):
        circles.clear()

# Clean
cv2.destroyAllWindows()
