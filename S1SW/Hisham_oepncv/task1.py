import cv2
import numpy as np

img1 = np.zeros((50, 50, 3), dtype=np.uint8)
img1[:] = [255, 0, 0]  

img2 = np.zeros((50, 50, 3), dtype=np.uint8)
img2[:] = [0, 255, 0]  

img3 = np.zeros((50, 50, 3), dtype=np.uint8)
img3[:] = [0, 0, 255]  

img4 = np.zeros((50, 50, 3), dtype=np.uint8)
img4[:] = [2, 25, 10]  

top_row = np.hstack((img1, img2)) 
bottom_row = np.hstack((img3, img4))  
combined_image = np.vstack((top_row, bottom_row)) 

resized_image = cv2.resize(combined_image, (200, 200), interpolation=cv2.INTER_NEAREST)

# Display the resulting image
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

