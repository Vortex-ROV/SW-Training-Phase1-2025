import cv2

def countingAndLabelling(contours, image):
    index = 1
    green_square_count = 0
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        X = int(x + w / 2)
        Y = int(y + h / 2)

        pixelColor = image[Y, X]
        b, g, r = pixelColor  

        if g > r and g > b:
            green_square_count += 1
            cv2.putText(image, str(index), (X, Y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
            index += 1

    return green_square_count

previousImage = cv2.imread(r'seagrass_images\new_0.png')
newImage = cv2.imread(r'seagrass_images\new_1.png')

grayPrevious = cv2.cvtColor(previousImage, cv2.COLOR_BGR2GRAY)
grayNew = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)

edgesPrevious = cv2.Canny(grayPrevious, 30, 100)
edgesNew = cv2.Canny(grayNew, 30, 100)

contoursPrevious, _ = cv2.findContours(edgesPrevious, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contoursNew, _ = cv2.findContours(edgesNew, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

previousGreenCount = countingAndLabelling(contoursPrevious, previousImage)
newGreenCount = countingAndLabelling(contoursNew, newImage)

print(f"Number of green squares in previous image: {previousGreenCount}")
print(f"Number of green squares in new image: {newGreenCount}")

cv2.imshow("Previous Image", previousImage)
cv2.imshow("New Image", newImage)

if ((previousGreenCount - newGreenCount) > 0):
    print(f"There are more seagrass as the number increased by {previousGreenCount - newGreenCount}.")
else:
    print(f"There are less seagrass as the number decreased by {abs(previousGreenCount - newGreenCount) }.")


cv2.waitKey(0)
cv2.destroyAllWindows()
