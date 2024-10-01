import cv2

cap = cv2.VideoCapture(0)
is_recording = False
video_writer = None

fourcc = cv2.VideoWriter_fourcc(*'XVID')

rotate_flag = False
show_all_flag = False
grayscale_flag = False
hsv_flag = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if rotate_flag:
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    original_frame = frame.copy()

    gray_frame = cv2.cvtColor(original_frame, cv2.COLOR_BGR2GRAY)
    hsv_frame = cv2.cvtColor(original_frame, cv2.COLOR_BGR2HSV)

    gray_display = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)

    gray_display = cv2.resize(gray_display, (original_frame.shape[1], original_frame.shape[0]))
    hsv_display = cv2.resize(hsv_frame, (original_frame.shape[1], original_frame.shape[0]))
    rotated_display = cv2.resize(frame, (original_frame.shape[1], original_frame.shape[0]))
    original_display = cv2.resize(original_frame, (original_frame.shape[1], original_frame.shape[0]))

    if grayscale_flag:
        cv2.imshow('Grayscale Frame', gray_display)
    elif hsv_flag:
        cv2.imshow('HSV Frame', hsv_display)
    else:
        cv2.imshow('Original Frame', original_display)

    if show_all_flag:
        top_combined = cv2.hconcat([gray_display, hsv_display])
        bottom_combined = cv2.hconcat([rotated_display, original_display])
        combined_view = cv2.vconcat([top_combined, bottom_combined])
        cv2.imshow('Combined View', combined_view)

    if is_recording and video_writer is not None:
        video_writer.write(original_frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('r'):
        rotate_flag = not rotate_flag
    elif key == ord('c'):
        cv2.imwrite('saved_frame.png', frame)
        print("Frame saved as 'saved_frame.png'")
    elif key == ord('s'):
        if not is_recording:
            is_recording = True
            video_writer = cv2.VideoWriter('output_video.avi', fourcc, 20.0, (frame.shape[1], frame.shape[0]))
            print("Started recording video.")
        else:
            is_recording = False
            video_writer.release()
            video_writer = None
            print("Stopped recording video.")
    elif key == ord('g'):
        grayscale_flag = not grayscale_flag
        hsv_flag = False
    elif key == ord('h'):
        hsv_flag = not hsv_flag
        grayscale_flag = False
    elif key == ord('x'):
        show_all_flag = not show_all_flag
        grayscale_flag = False
        hsv_flag = False
    elif key == ord('z'):
        show_all_flag = False
        grayscale_flag = False
        hsv_flag = False

cap.release()
if video_writer is not None:
    video_writer.release()
cv2.destroyAllWindows()
