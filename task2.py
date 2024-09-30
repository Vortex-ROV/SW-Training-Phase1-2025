import cv2
import numpy as np

cap = cv2.VideoCapture(0) #bswr
if not cap.isOpened():
    print('error:camera could not open')
    exit()
   
show_HSV = False
show_rotate = False
show_grey = False
show_original = False
save_video = False
out = None 

while True:
    
    ret, frame = cap.read() #b2ra ele sawrto
    if not ret:
        print('error:could not read frame')
        break
    display_frame = frame.copy()
    
    
    if show_HSV:
        display_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)  
    if show_rotate:
        display_frame = cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
    if show_grey:
        display_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        display_frame = cv2.cvtColor(display_frame, cv2.COLOR_GRAY2BGR) 
    if show_original:
        display_frame = frame

    cv2.imshow('Video Capture', display_frame)    

    #cv2.imshow('Video Capture', frame)
    key = cv2.waitKey(1)& 0xff
    if   key ==ord('q'):
         break  
    elif key ==ord('c'): #save the frame in device
        cv2.imwrite('snapshot.jpg',frame)
    elif key ==ord('h'): #convert to HSV space 
        show_HSV      = not show_HSV
        show_grey     =False
        show_original =False
        show_rotate   =False       
    elif key ==ord('s'): #save a video stream using OpenCV
        if not save_video:  # Start saving video
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
            save_video = True
        out.write(frame)
    elif key ==ord('r'): #rotate
        show_HSV      =False
        show_grey     =False
        show_original =False
        show_rotate   = not show_rotate        
    elif key ==ord('g'): #convert to grayscale
        show_grey     = not show_grey
        show_HSV      = False
        show_original =False
        show_rotate   =False
         
    elif key ==ord('z'): #show original frame
        show_original = not show_original
        show_grey     =False
        show_HSV      =False
        show_rotate   =False
         
    elif key == ord('x'):  
        rotate = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        grey1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        grey2 = cv2.cvtColor(grey1, cv2.COLOR_GRAY2BGR)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #resize(shape,width,height)
        rotate = cv2.resize(rotate,  (200,200))   
        grey2 = cv2.resize(grey2,  (200,200))
        hsv = cv2.resize(hsv, (200,200))
        frame = cv2.resize(frame, (200,200))

        concatenated_hz = cv2.hconcat([rotate, grey2, hsv, frame])
        concatenated_hz = cv2.resize(concatenated_hz,(800,200))
        cv2.imshow('Concatenated Frames', concatenated_hz)  # Give the window a name
        cv2.waitKey(8000)  # Show for 5 seconds
        cv2.destroyAllWindows()  
        
if save_video and out is not None:
   out.release()
cap.release()
cv2.destroyAllWindows()