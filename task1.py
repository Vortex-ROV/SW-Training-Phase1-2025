import cv2
import numpy as np

red = np.zeros((50, 50, 3), dtype=np.uint8)
red[:] = [0, 0, 255] 

green = np.zeros((50, 50, 3), dtype=np.uint8)
green[:] = [0, 255, 0] 

blue = np.zeros((50, 50, 3), dtype=np.uint8)
blue[:] = [255, 0, 0] 

yellow = np.zeros((50, 50, 3), dtype=np.uint8)
yellow[:] = [0, 255, 255]  


top_row = np.hstack((red, green))   
bottom_row = np.hstack((blue, yellow))  
combined_image = np.vstack((top_row, bottom_row))  

resized_image = cv2.resize(combined_image, (200, 200))

cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
