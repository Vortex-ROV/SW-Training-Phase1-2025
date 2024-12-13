import cv2
import numpy as np

image_height = 50
image_width = 50


blueImage = np.zeros((image_height,image_width,3), np.uint8)
blueImage[:,:,0]=255
blueImage[:,:,1]=0
blueImage[:,:,2]=0

redImage = np.zeros((image_height,image_width,3), np.uint8)
redImage[:,:,0]=0
redImage[:,:,1]=0
redImage[:,:,2]=255

greenImage = np.zeros((image_height,image_width,3), np.uint8)
greenImage[:,:,0]=0
greenImage[:,:,1]=255
greenImage[:,:,2]=000

whiteImage = np.zeros((image_height,image_width,3), np.uint8)
whiteImage[:,:,0]=255
whiteImage[:,:,1]=255
whiteImage[:,:,2]=255

row1 = np.concatenate((blueImage, redImage), axis=0)
row2 = np.concatenate((greenImage, whiteImage), axis=0)

final_img = np.concatenate((row1, row2), axis=1)
resized_img = cv2.resize(final_img, (200,200))

height, width, channels = final_img.shape
resized_height, resized_width, resized_channels = resized_img.shape

print(height, width, channels)
print(resized_height, resized_width, resized_channels)

cv2.imshow("Final Image", final_img)
cv2.imshow("Resized Image", resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()