import time
import cv2

def Terminate_Stream(stream):
    stream.release()
    cv2.destroyAllWindows() 

def Rotate_90(frame):
    return cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

def Save_Frame(frame):
    cv2.imwrite("save_frame.jpg",frame)
    print("Frame Saved")
    pass

def Save_video_stream(frame):
    pass

def Convert_To_Greyscale(frame):
    pass

def Convert_To_HSV(frame):
    pass


stream = cv2.VideoCapture(0)
while True:
    ret, frame = stream.read()
    cv2.imshow("Main Camera",frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        Terminate_Stream(stream)
        time.sleep(500)
        break
    elif cv2.waitKey(1) & 0xFF == ord('r'):
        rotated_frame = Rotate_90(frame)
        cv2.imshow("Rotate Frame", rotated_frame)
        time.sleep(1000)
    elif cv2.waitKey(1) & 0xFF == ord('c'):
        Save_Frame(frame)
    elif cv2.waitKey(1) & 0xFF == ord('s'):
        Save_video_stream(frame)
    elif cv2.waitKey(1) & 0xFF == ord('g'):
        Convert_To_Greyscale(frame)
    elif cv2.waitKey(1) & 0xFF == ord('h'):
        Convert_To_HSV(frame)
    


