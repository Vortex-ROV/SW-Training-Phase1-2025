import cv2
import numpy as np
import matplotlib.pyplot as plt


# Function to convert an image into an 8x8 grid representing seagrass bed
def preprocess_image(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Resize the image to 8x8 grid
    resized_img = cv2.resize(img, (8, 8), interpolation=cv2.INTER_AREA)

    # Convert to HSV to better differentiate green seagrass from other colors
    hsv_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)

    # Define the range for green in color space
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])

    # Create a mask that identifies green areas in the image
    mask = cv2.inRange(hsv_img, lower_green, upper_green)

    # Convert the mask to binary: 1 for green, 0 for non-green - white areas
    grid = (mask > 0).astype(int)

    return grid


# Load and preprocess both images
prior_image_path = "original.png"
current_image_path = "new_55.png"

prior_grid = preprocess_image(prior_image_path)
current_grid = preprocess_image(current_image_path)


# Compare the two grids
def compare_grids(prior, current):
    recovery = np.sum((prior == 0) & (current == 1))  # white to green
    decrease = np.sum((prior == 1) & (current == 0))  # green to white
    return recovery, decrease


recovery, decrease = compare_grids(prior_grid, current_grid)

# Display the comparison results
print(f"Number of squares recovered (white to green): {recovery}")
print(f"Number of squares decreased (green to white): {decrease}")

# Visualize the grids for both 
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].imshow(prior_grid, cmap='Greens', vmin=0, vmax=1)
axs[0].set_title('Prior Seagrass Grid (3 months ago)')
axs[0].axis('off')

axs[1].imshow(current_grid, cmap='Greens', vmin=0, vmax=1)
axs[1].set_title('Current Seagrass Grid')
axs[1].axis('off')

plt.show()

# Save the resulting image as output
output_path = "comparison_output.png"  # Save as PNG
comparison_image = np.hstack([prior_grid * 255, current_grid * 255])
cv2.imwrite(output_path, comparison_image)
print(f"Comparison image saved at {output_path}")
