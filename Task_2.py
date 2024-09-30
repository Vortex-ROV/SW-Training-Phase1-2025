import cv2

# Initialize camera capture
# i use argument 0 cuz This opens the default camera (webcam) for capturing video.
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Changed from XVID to mp4v
out = None
recording = False

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break

    # Display the original frame
    cv2.imshow('Original Frame', frame)

    key = cv2.waitKey(1) & 0xFF

    #  'Q' to quit
    if key == ord('q'):
        break
    # Press 'R' to rotate the frame 90 degrees
    elif key == ord('r'):
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow('Rotated Frame', frame)
    #  'C' to save the current frame
    elif key == ord('c'):
        cv2.imwrite('saved_frame.png', frame)
        print("Frame saved as 'saved_frame.png'")
    # Press 'S' to start/stop video recording
    elif key == ord('s'):
        if not recording:
            out = cv2.VideoWriter('output_video.mp4', fourcc, 20.0, (frame.shape[1], frame.shape[0]))
            recording = True
            print("Recording started")
        else:
            recording = False
            out.release()
            print("Recording stopped")
    # 'G' to convert the frame to grayscale
    elif key == ord('g'):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Grayscale Frame', gray_frame)
    # Press 'H' to convert the frame to HSV space
    elif key == ord('h'):
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow('HSV Frame', hsv_frame)
    # 'X' to display grayscale, HSV, rotated, and original together
    elif key == ord('x'):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

        combined_frame = cv2.hconcat([frame, cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR), hsv_frame, rotated_frame])
        cv2.imshow('Combined Frames', combined_frame)
    # 'Z' to show only the original frame
    elif key == ord('z'):
        cv2.imshow('Original Frame', frame)

    # Save the video stream if recording
    if recording:
        out.write(frame)

# Release everything once done
cap.release()
if recording:
    out.release()
cv2.destroyAllWindows()
