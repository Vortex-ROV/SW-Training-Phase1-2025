import cv2

image = cv2.imread(r'Tasks_Images2025\task_7\shapes_sizes.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 30, 100)

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

index = 1  

for contour in sorted_contours:
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

    x, y, w, h = cv2.boundingRect(contour)
    X = int(x + w / 2)
    Y = int(y + h / 2)
        
    cv2.putText(image, str(index), (X, Y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)  
    index += 1

cv2.imshow("gray",gray)
cv2.imshow('Sorted Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
