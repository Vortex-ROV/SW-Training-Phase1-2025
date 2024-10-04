import cv2
import numpy as np

points = []

def select_points(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN and len(points) < 4:
        points.append((x, y))
        print(f"Point selected: {x}, {y}")

image_path = "S1SW/Hisham_oepncv/computer vision.PNG"  
image = cv2.imread(image_path)

image = cv2.resize(image, (800, 600))

cv2.namedWindow("Select Points")
cv2.setMouseCallback("Select Points", select_points)

while True:
    for point in points:
        cv2.circle(image, point, 5, (0, 0, 255), -1)
    
    cv2.imshow("Select Points", image)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q') or len(points) == 4:  
        break

cv2.destroyAllWindows()


if len(points) == 4:
    pts_src = np.array(points, dtype="float32")
    width = 700  
    height = 500  
    pts_dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype="float32")

    matrix = cv2.getPerspectiveTransform(pts_src, pts_dst)

    warped_image = cv2.warpPerspective(image, matrix, (width, height))

    cv2.imshow("Bird's Eye View", warped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Four points were not selected.")
