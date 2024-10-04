import cv2
import numpy as np

image_path = "S1SW/Hisham_oepncv/shapes_sizes.png"  # Ensure this path is correct
image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contour_areas = [(cv2.contourArea(c), c) for c in contours]
contour_areas.sort(key=lambda x: x[0], reverse=True)  

for index, (area, contour) in enumerate(contour_areas):
    cv2.drawContours(image, [contour], -1, (0, 80,60), 2)  
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.putText(image, f"Order: {index + 1}", (cX - 20, cY - 20), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

cv2.imshow("Contours Sorted by Order", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
