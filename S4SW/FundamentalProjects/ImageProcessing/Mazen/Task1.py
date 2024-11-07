import cv2
import numpy as np

# Step 1: Create 4 images, each 50x50 with distinct colors (Red, Green, Blue, Yellow)
color_values = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (0, 255, 255)]  # BGR format for OpenCV
images = [np.full((50, 50, 3), color, dtype=np.uint8) for color in color_values]

# Step 2: Attach the 4 images to make a 100x100 image
# Combining the images horizontally and vertically to form a 100x100 grid
top_row = np.hstack((images[0], images[1]))  # Top-left and Top-right
bottom_row = np.hstack((images[2], images[3]))  # Bottom-left and Bottom-right
combined_image = np.vstack((top_row, bottom_row))  # Combine top and bottom rows vertically

# Step 3: Resize the combined image to 200x200
resized_image = cv2.resize(combined_image, (200, 200), interpolation=cv2.INTER_LINEAR)

# Save the image to file for verification
resized_image_path = "task1____.png"
cv2.imwrite(resized_image_path, resized_image)

cv2.imshow('image',resized_image)
cv2.waitKey(0)
