import cv2
import numpy as np

# Initialize list to store points
points = []

def click_event(event, x, y, flags, param):
    global points
    # Capture the points on left mouse button click
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 4:
            points.append((x, y))
            cv2.circle(img, (x, y), 10, (255, 255, 0), 3)
            cv2.imshow("Image", img)
            print(f"Point {len(points)}: {x, y}")

# Load the image
img = cv2.imread("Cards.jpg")
arrow_img = cv2.imread("Arrow.jpg")
cv2.imshow("Image", img)

# Set the mouse callback function to capture points
cv2.setMouseCallback("Image", click_event)

# Wait until four points are selected
while True:
    if len(points) == 4:
        break
    cv2.waitKey(1)

# Define output image size for bird's eye view
width, height = 300, 200

# Define destination points for bird's eye view
dst_points = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype="float32")

# Convert selected points to a numpy array
src_points = np.array(points, dtype="float32")

# Calculate perspective transform matrix
matrix = cv2.getPerspectiveTransform(src_points, dst_points)

# Apply the perspective transformation
bird_eye_view = cv2.warpPerspective(img, matrix, (width, height))

# Resize bird's eye view, arrow, and original images to a width of 300 and original height
new_width = 450
bird_eye_resized  = cv2.resize(bird_eye_view, (new_width, img.shape[0]))
img_resized       = cv2.resize(img, (new_width, img.shape[0]))  
arrow_img_resized = cv2.resize(arrow_img, (new_width, img.shape[0]))

# Combine original and transformed views side by side
combined_img = np.hstack((img_resized, arrow_img_resized ,bird_eye_resized))

# Display the combined image
cv2.imshow("Original and Bird's Eye View", combined_img)

print("Original image shape:", img_resized.shape)
print("Arrow image shape:", bird_eye_resized.shape)
print("Bird's eye view shape:", bird_eye_resized.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()
