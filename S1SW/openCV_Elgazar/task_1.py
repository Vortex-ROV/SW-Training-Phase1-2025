import numpy as np
import cv2
from matplotlib import pyplot as plt

# Define the four distinct colors in BGR format
colors = [
    (255, 0, 0),   # Blue
    (0, 255, 0),   # Green
    (0, 0, 255),   # Red
    (0, 0, 0)  	   # Black
]

# Create 4 separate images of 50x50 with distinct colors
image1 = np.full((50, 50, 3), colors[0], dtype=np.uint8)
image2 = np.full((50, 50, 3), colors[1], dtype=np.uint8)
image3 = np.full((50, 50, 3), colors[2], dtype=np.uint8)
image4 = np.full((50, 50, 3), colors[3], dtype=np.uint8)

# Combine images to create a 100x100 image
top_row = np.hstack((image1, image2))
bottom_row = np.hstack((image3, image4))
combined_image = np.vstack((top_row, bottom_row))

# Resize the image to 200x200
resized_image = cv2.resize(combined_image, (200, 200))

# Display the final resized image
plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
plt.title('Task 1')
plt.axis('off')
plt.show()
