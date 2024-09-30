import numpy as np
import cv2

img1 = np.full((50, 50, 3), (0, 0, 0), dtype=np.uint8)   
img2 = np.full((50, 50, 3), (255, 255, 0), dtype=np.uint8)   
img3 = np.full((50, 50, 3), (0, 0, 255), dtype=np.uint8)   
img4 = np.full((50, 50, 3), (255, 255, 255), dtype=np.uint8) 
top_row = np.hstack((img1, img2))  
bottom_row = np.hstack((img3, img4))  
combined_image = np.vstack((top_row, bottom_row)) 
resized_image = cv2.resize(combined_image, (200, 200))
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
