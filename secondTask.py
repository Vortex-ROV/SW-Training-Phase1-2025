import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None
saving_video = False

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting ...")
        break

    cv2.imshow('Original', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'): 
        break

    elif key == ord('r'):  
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow('Rotated', frame)

    elif key == ord('g'):  
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Grayscale', gray_frame)

    elif key == ord('h'): 
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow('HSV', hsv_frame)

    elif key == ord('x'):  
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

        combined_frame = cv2.hconcat([cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR),
                                      hsv_frame, rotated_frame, frame])
        cv2.imshow('Combined', combined_frame)

    elif key == ord('z'):  
        cv2.imshow('Original', frame)

    elif key == ord('c'):  
        cv2.imwrite('captured_frame.jpg', frame)
        print("Frame saved as captured_frame.jpg")

    elif key == ord('s'): 
        if not saving_video:
            out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame.shape[1], frame.shape[0]))
            saving_video = True
            print("Started saving video...")

    elif key == ord('e'):  
        if saving_video:
            saving_video = False
            out.release()
            print("Stopped saving video.")

    if saving_video:
        out.write(frame)

cap.release()
if saving_video:
    out.release()
cv2.destroyAllWindows()
