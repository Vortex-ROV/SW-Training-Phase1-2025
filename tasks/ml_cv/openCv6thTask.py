import cv2
import numpy as np
import matplotlib.pyplot as plt

def preprocess_image(image_path):
    
    img = cv2.imread(image_path)

    resized_img = cv2.resize(img, (8, 8), interpolation=cv2.INTER_AREA)

    hsv_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)

    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])

    mask = cv2.inRange(hsv_img, lower_green, upper_green)

    grid = (mask > 0).astype(int)

    return grid

prior_grid = preprocess_image("tasks\ml_cv\original.png")
current_grid = preprocess_image("tasks\ml_cv\\new_27.png")


def compare_grids(prior, current):
    recovery = np.sum((prior == 0) & (current == 1)) 
    decrease = np.sum((prior == 1) & (current == 0))  
    return recovery, decrease


recovery, decrease = compare_grids(prior_grid, current_grid)

print(f"Number of squares recovered : {recovery}")
print(f"Number of squares decreased : {decrease}")

fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].imshow(prior_grid, cmap='Greens', vmin=0, vmax=1)
axs[0].set_title('Prior Seagrass Grid (3 months ago)')
axs[0].axis('off')

axs[1].imshow(current_grid, cmap='Greens', vmin=0, vmax=1)
axs[1].set_title('Current Seagrass Grid')
axs[1].axis('off')

plt.show()

output_path = "comparison_output.png" 
comparison_image = np.hstack([prior_grid * 255, current_grid * 255])
cv2.imwrite(output_path, comparison_image)
print(f"Comparison image saved at {output_path}")
