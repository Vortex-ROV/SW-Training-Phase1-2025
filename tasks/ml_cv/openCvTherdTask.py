import cv2
import numpy as np

x = int(input("Enter the x-coordinate of the float: "))
y = int(input("Enter the y-coordinate of the float: "))
shift_direction = input("Do you want the float to move 'up' or 'down'? ").lower()
value = int(input("Enter the shift value: "))
if shift_direction == 'up':
    newY = y - value
elif shift_direction == 'down':
    newY = y + value
grid_size = 500  
grid = np.ones((grid_size, grid_size, 3), dtype=np.uint8) * 255 
cv2.circle(grid, (x, y), 5, (255, 0, 0), -1)  
cv2.putText(grid, "Current Position", (x + 10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0, 0), 1)
cv2.circle(grid, (x, newY), 5, (0, 255, 0), -1)  
cv2.putText(grid, "New Position", (x + 10, newY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0,0), 1)
for i in range(0, grid_size, 20):  
    cv2.line(grid, (i, 0), (i, grid_size), (200, 200, 200), 1) 
    cv2.line(grid, (0, i), (grid_size, i), (200, 200, 200), 1)  
cv2.imshow("Float Positions on Grid", grid)
cv2.waitKey(0)
cv2.destroyAllWindows()
