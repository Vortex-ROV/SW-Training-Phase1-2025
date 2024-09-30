import cv2
import numpy as np

# Ask the user for the current position (x, y)
current_x = int(input("Enter the current x-coordinate of the float: "))
current_y = int(input("Enter the current y-coordinate of the float: "))

# Ask the user for the desired vertical shift (above or below)
shift_direction = input("Do you want the float to move 'above' or 'below' the current position? ").lower()
shift_value = int(input("Enter the vertical shift value: "))

# Determine the new position
if shift_direction == 'above':
    new_y = current_y - shift_value
elif shift_direction == 'below':
    new_y = current_y + shift_value
else:
    print("Invalid direction. Please enter 'above' or 'below'.")
    exit()

# Create a grid image using OpenCV
grid_size = 500  # Define the size of the grid
grid = np.ones((grid_size, grid_size, 3), dtype=np.uint8) * 255  # White background

# Draw the current position of the float
cv2.circle(grid, (current_x, current_y), 5, (255, 0, 0), -1)  # Blue for the current position
cv2.putText(grid, "Current Position", (current_x + 10, current_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

# Draw the new position of the float
cv2.circle(grid, (current_x, new_y), 5, (0, 255, 0), -1)  # Green for the new position
cv2.putText(grid, "New Position", (current_x + 10, new_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

# Draw grid lines
for i in range(0, grid_size, 20):  # Every 50 pixels
    cv2.line(grid, (i, 0), (i, grid_size), (200, 200, 200), 1)  # Vertical lines
    cv2.line(grid, (0, i), (grid_size, i), (200, 200, 200), 1)  # Horizontal lines

# Display the grid with the positions
cv2.imshow("Float Positions on Grid", grid)

# Wait until any key is pressed and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
