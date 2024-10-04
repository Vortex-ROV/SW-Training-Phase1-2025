import cv2
import numpy as np


camera = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('test.avi', fourcc, 20.0, (640, 480))

saveVideo = False
rotateFrame = False

i = 0
while camera.isOpened():
    i += 1
    ret, frame = camera.read()
    
    if ret:

        if rotateFrame:
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

        cv2.imshow('Original Frame', frame)
        
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('q'):  
            break

        elif key == ord('r'):  # Rotate frame
            if rotateFrame:
                rotateFrame = False 
            else:
                rotateFrame = True 

        elif key == ord('c'):  
            cv2.imwrite(f'saved_frame{i}.jpg', frame)
            print(f"Frame saved as 'saved_frame{i}.jpg'.")

        elif key == ord('s'):  

            if saveVideo:
                saveVideo = False 
            else:
                saveVideo = True 

            if saveVideo:
                print(f"Started video recording...")
            else:
                print(f"Stopped video recording...")

        elif key == ord('g'):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Grayscale Frame', gray)

        elif key == ord('h'): 
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            cv2.imshow('HSV Frame', hsv)

        elif key == ord('x'):  
            grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            grayFrameBgr = cv2.cvtColor(grayFrame, cv2.COLOR_GRAY2BGR)
            combined = np.hstack((frame, grayFrameBgr, hsvFrame))
            cv2.imshow('Combined Frames', combined)
                
        elif key == ord('z'):
            cv2.destroyAllWindows()
            cv2.imshow('Original Frame', frame)

        if saveVideo: 
            out.write(frame)
            
    else:
        break

out.release()
camera.release()
cv2.destroyAllWindows()
