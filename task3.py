import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

def Draw_Position (Current,Next):
    cv2.circle(img,Current,7,(255,0,0),-1)
    cv2.putText(img, 'Current Position', (Current[0] + 10, Current[1] - 10),
             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    cv2.circle(img,Next,7,(0,255,0),-1)
    cv2.putText(img, 'Surfacing Position', (Next[0] + 10, Next[1] - 10),
             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv2.imshow('image',img)

CurrentPosition_X = int(input('enter the current position (x coordinate)(0-511): ').strip())
CurrentPosition_Y = int(input('enter the current position (Y coordinate)(0-511): ').strip())

CurrentPosition = (CurrentPosition_X , CurrentPosition_Y)
while True:
    Distance_DIR =input('please choose the next srfacing position 1)above the current position 2)below the current position')
    if Distance_DIR =='1':
        Distance = int(input('enter the distance to the next surfacing position above the current postion: '))
        NextPosition = (CurrentPosition_X , CurrentPosition_Y - int(Distance))
        if NextPosition[1] < 0:
                print("Surfacing position is out of bounds. Adjusting to (X, 0).")
                NextPosition = (CurrentPosition_X, 0)
        break
    elif Distance_DIR =='2':
        Distance = int(input('enter the distance to the next surfacing position below the current postion: '))
        NextPosition = (CurrentPosition_X , CurrentPosition_Y + int(Distance))
        if NextPosition[1] > 511:
                print("Surfacing position is out of frame. Adjusting to (X, 511).")
                NextPosition = (CurrentPosition_X, 511)
            
        break
    else :
        print('invalid choice please enter 1) or 2)')
        

    
Draw_Position(CurrentPosition , NextPosition)

cv2.waitKey(0)
cv2.destroyAllWindows()

