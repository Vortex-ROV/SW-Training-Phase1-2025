import cv2
import numpy as np
import os 
import random
image1 = cv2.imread('E:/vortex peri/OpenCVExample/Tasks_Images2025/task_6/original.png')
folder_path= 'OpenCVExample/Tasks_Images2025/task_6/seagrass_images'
#image2 = cv2.imread('E:/vortex peri/OpenCVExample/Tasks_Images2025/task_6/seagrass_images/new_0.png')

imgray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
folder_list =[filename for filename in os.listdir(folder_path) ]
if folder_list:
    randome_image = random.choice(folder_list)
    image_path = os.path.join(folder_path, randome_image)
    image2 = cv2.imread(image_path)
# Check if images are loaded
    if image1 is None or image2 is None:
        print("Error: One or both images could not be loaded.")
        exit()
    #imgray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    imgray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    imgray2 = cv2.resize(imgray2, (imgray1.shape[1],imgray1.shape[0]))

    difference = cv2.absdiff(imgray1, imgray2)
    _, thresh = cv2.threshold(difference, 30, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# loop through each contour (shape)
    for i, contour in enumerate(contours):
        mask = np.zeros(imgray1.shape, dtype=np.uint8)  # Create a mask for the current shape
        cv2.drawContours(mask, contours, i, 255, -1)  # Fill the shape in the mask
        shape_pixels_changed = cv2.countNonZero(cv2.bitwise_and(thresh, mask))    #Count changed pixels within the shape using the thresholded difference

total_pixels_changed = cv2.countNonZero(thresh)  #count total num of pixels changed 
if total_pixels_changed ==0 or shape_pixels_changed ==0:
    print("no difference in any squares")



#print(f"Number of different pixels: {num_different_pixels}")
else:
    number_of_changed_squares=int(total_pixels_changed/shape_pixels_changed)
    print(f"{number_of_changed_squares} square/s of seagrass has been changed ")

#cv2.imshow("Difference", difference)
#cv2.imshow("Threshold", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
