import cv2

# Initialize video capture and writer
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None  # Placeholder for the video writer

rotate_flag = False
save_vid_flag = False

# Set video frame dimensions
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 700)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 700)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply rotation if R is pressed
    if rotate_flag:
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    # Show the original frame
    cv2.imshow('Frame', frame)

    # Get the key input
    key = cv2.waitKey(1) & 0xFF

    # Quit the program
    if key == ord('q'):
        break

    # Toggle video recording on 's' key press
    elif key == ord('s'):
        save_vid_flag = not save_vid_flag
        if save_vid_flag:
            out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame.shape[1], frame.shape[0]))
            print("Video recording started")
        else:
            out.release()
            print("Video recording stopped")

    # Save current frame as an image on 'c' key press
    elif key == ord('c'):
        cv2.imwrite('saved_image.jpg', frame)
        print("Frame saved as 'saved_image.jpg'")

    # Toggle rotation on 'r' key press
    elif key == ord('r'):
        rotate_flag = not rotate_flag

    # Show grayscale frame on 'g' key press
    elif key == ord('g'):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Grayscale Frame', gray_frame)

    # Show HSV frame on 'h' key press
    elif key == ord('h'):
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow('HSV Frame', hsv_frame)

    # Show all frames (grayscale, HSV, rotated, and original) together on 'x' key press
    elif key == ord('x'):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE) if rotate_flag else frame

        # Ensure frames are resized and converted to the same format
        height, width = frame.shape[:2]
        gray_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)  # Convert grayscale to 3-channel BGR
        hsv_frame = cv2.resize(hsv_frame, (width, height))
        rotated_frame = cv2.resize(rotated_frame, (width, height))

        # Concatenate all views horizontally
        combined_frame = cv2.hconcat([gray_frame, hsv_frame, rotated_frame, frame])
        cv2.imshow('Combined Views', combined_frame)

    # Show only the original frame on 'z' key press
    elif key == ord('z'):
        cv2.destroyAllWindows()
        cv2.imshow('Frame', frame)

    # Save the frame if video recording is active
    if save_vid_flag:
        out.write(frame)

# Release everything once done
cap.release()
if out:
    out.release()
cv2.destroyAllWindows()
