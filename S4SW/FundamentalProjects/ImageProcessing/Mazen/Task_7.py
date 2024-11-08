import cv2

# Load the image
img = cv2.imread("saved_image.jpg", 1)

# Convert the image to grayscale
grey_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a binary threshold to the grayscale image
_, thres_image = cv2.threshold(grey_image, 180, 255, cv2.THRESH_BINARY_INV)

# Find contours on the thresholded image
contours, _ = cv2.findContours(thres_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours by area in descending order
sorted_con = sorted(contours, key=cv2.contourArea, reverse=True)

# Draw the sorted contours on the original image
for i, contour in enumerate(sorted_con):
    color = (0, 255, 0)  # Green color
    cv2.drawContours(img, [contour], -1, color, 2)
    area = cv2.contourArea(contour)
    print(f"Contour {i + 1} area: {area}")

# Display the image with contours
cv2.imshow("Contours (sorted by area)", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
