import cv2

cap = cv2.VideoCapture(0)

video_writer = None
saving_video = False

while cap.isOpened():
    ret, frame = cap.read()

    cv2.imshow('Original Frame', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    elif key == ord('r'):
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow('Rotated Frame', frame)

    elif key == ord('c'):
        save_path = '/mnt/data/saved_frame.jpg'
        cv2.imwrite(save_path, frame)
        print(f"Frame saved at {save_path}.")

    elif key == ord('s'):
        if saving_video:
            saving_video = False
            video_writer.release()
            print("Stopped saving video.")
        else:
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            video_writer = cv2.VideoWriter('./S5SW/ML-Tasks/saved_video.avi', fourcc, 20.0, (frame.shape[1], frame.shape[0]))
            saving_video = True
            print("Started saving video.")

    if saving_video and video_writer:
        video_writer.write(frame)


    elif key == ord('g'):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Grayscale Frame', gray_frame)

    elif key == ord('h'):
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow('HSV Frame', hsv_frame)

    elif key == ord('x'):
        rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow('Rotated Frame', rotated_frame)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Grayscale Frame', gray_frame)
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow('HSV Frame', hsv_frame)
        cv2.waitKey(0)
        cv2.destroyWindow("Rotated Frame")
        cv2.destroyWindow("Grayscale Frame")
        cv2.destroyWindow("HSV Frame")
        

    elif key == ord('z'):
        cv2.destroyAllWindows()

cap.release()
if video_writer:
    video_writer.release()
cv2.destroyAllWindows()
