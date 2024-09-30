import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

# List to store the four points selected on the card
points = []


# Mouse callback function to select points
def select_points(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN and len(points) < 4:
        points.append((x, y))
        print(f"Point selected: {(x, y)}")


# Function to open file dialog and load the image
def load_image():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select an Image",
                                           filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
    return file_path


# Function to save the output image
def save_output(image, filename):
    cv2.imwrite(filename, image)
    print(f"Output saved as '{filename}'")


# Load the image using the file dialog
image_path = load_image()
if not image_path:
    print("No image selected, exiting.")
    exit()

# Read the selected image
image = cv2.imread(image_path)

# Create a window and set the mouse callback to capture points
cv2.namedWindow('Select 4 Points')
cv2.setMouseCallback('Select 4 Points', select_points)

while True:
    # Display the image and the selected points
    img_copy = image.copy()
    for point in points:
        cv2.circle(img_copy, point, 5, (0, 255, 0), -1)  # Draw selected points

    cv2.imshow('Select 4 Points', img_copy)

    # Press 'q' to quit after selecting 4 points
    if cv2.waitKey(1) & 0xFF == ord('q') and len(points) == 4:
        break

# Close the window
cv2.destroyAllWindows()

# Perform perspective transformation if 4 points are selected
if len(points) == 4:
    # Define the points in the destination (bird's-eye view)
    width, height = 600, 600  # Set the desired output size (increased width and height)
    dst_points = np.array([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]], dtype="float32")

    # Convert the selected points into a NumPy array
    src_points = np.array(points, dtype="float32")

    # Compute the perspective transform matrix
    matrix = cv2.getPerspectiveTransform(src_points, dst_points)

    # Perform the perspective warp to get the bird's-eye view
    bird_eye_view = cv2.warpPerspective(image, matrix, (width, height))

    # Show the bird's-eye view result
    cv2.imshow('Bird\'s Eye View', bird_eye_view)

    # Save the output image
    output_filename = "bird_eye_view.png"
    save_output(bird_eye_view, output_filename)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: You must select exactly 4 points.")
