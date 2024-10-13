import cv2
import numpy as np


# Function to load the image and preprocess it
def load_and_preprocess_image(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply edge detection
    edged = cv2.Canny(blurred, 50, 150)

    return img, edged


# Function to find and sort contours
def find_and_sort_contours(edged_image):
    # Find contours
    contours, _ = cv2.findContours(edged_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sort contours by area in descending order
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    return contours


# Function to draw contours on the original image
def draw_contours(image, contours):
    for i, contour in enumerate(contours):
        # Draw each contour
        cv2.drawContours(image, contours, i, (0, 255, 0), 2)  # Green color for contours
        # Put the index of the contour
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.putText(image, str(i + 1), (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)


# Main execution
image_path = "shapes_sizes.png"  # Replace with your image path

# Load and preprocess the image
original_image, edged_image = load_and_preprocess_image(image_path)

# Find and sort contours
contours = find_and_sort_contours(edged_image)

# Draw sorted contours on the original image
draw_contours(original_image, contours)

# Save the output image with contours
output_path = "output_contours.png"  # Change this to your desired output path
cv2.imwrite(output_path, original_image)

# Display the original image with contours
cv2.imshow("Contours Sorted by Area", original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print the areas of the contours
for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    print(f"Contour {i + 1}: Area = {area}")
