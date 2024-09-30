import cv2
import numpy as np

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None
recording = False

while True:

    ret, frame = cap.read()
    
    key = cv2.waitKey(1) & 0xFF

    cv2.imshow('Frame', frame)

    if key == ord('r'):
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    
    if key == ord('c'):
        cv2.imwrite('savedFrame.png', frame)
    
    if key == ord('s') and not recording:
        out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame.shape[1], frame.shape[0]))
        recording = True
    
    elif key == ord('s') and recording:
        recording = False
        out.release()
    
    if recording:
        out.write(frame)
    
    if key == ord('g'):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Grayscale Frame', gray_frame)
    
    if key == ord('h'):
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow('HSV Frame', hsv_frame)
    
    if key == ord('x'):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        gray_bgr = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)
        combined_frame = np.hstack((frame, gray_bgr, hsv_frame, rotated_frame))
        cv2.imshow('Combined Frames', combined_frame)

    if key == ord('z'):
        cv2.imshow('Frame', frame)

    if key == ord('q'):
        break


cap.release()
if recording:
    out.release()
cv2.destroyAllWindows()
