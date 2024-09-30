import numpy as np
import cv2

img=np.zeros((512,512,3),np.uint8)
points = []

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y),10,(0,0,255),1)
        points.append((x,y))
        print(f'{x},{y}')
        cv2.imshow('image',img)
        
cv2.imshow('image',img)

        
cv2.setMouseCallback('image',click_event)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key ==ord('d'):         #delete last point
       if points:
          removed = points.pop()
          img[:]=0
          for (x,y) in points:   
            cv2.circle(img, (x,y),10,(0,0,255),1)
          print (f'the removed circle coordinate : {removed}')
          cv2.imshow('image',img)
    if key ==ord('a'):     #delate all points
       if points:
          removed = points.clear()
          img[:]=0
          cv2.imshow('image',img)
  
    elif key == 27: 
        break

cv2.destroyAllWindows()

