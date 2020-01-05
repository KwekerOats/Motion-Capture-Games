import cv2
import numpy as np

cap = cv2.VideoCapture(0)

ave_x = []
ave_y = []
ave_x2 = []
ave_y2 = []
r = 0
x = 0
ave2 = 0

while(1):
    try:
        #median smoothing
        '''if len(ave_x) == 5:
            for y in ave_x:
                x += y
            ave_x2.append(x/5)
            for p in ave_y:
                r += p
            ave_y2.append(r/4)
            if len(ave_x2) == 2:
                if ave_x2[0] + 10 <= ave_x2[1]:
                    print('LEFT')
                elif ave_x[0] - 10 >= ave_x2[1]:
                    print('RIGHT')
                elif ave_y2[0] + 10 <= ave_y2[1]:
                    print('UP')
                elif ave_y2[0] - 10 >= ave_y2[1]:
                    print('DOWN')
                ave_x2, ave_y2 = [],[]
            ave_x = []
            ave_y = []
            x = 0
            r = 0
        ave_x.append(coord[0][0][0])
        ave_y.append(coord[0][0][1])'''

        #moving average smoothing
        try:
            t02 = t01
        except:
            print('connecting')
        try:
            t01 = t
        except:
            print('connecting')
        try:
            t = t1
        except:
            print('connecting')
        try:
            t1 = t2
        except:
            print('connecting')
        t2 = coord[0][0][0]

        ave1 = (t02+t01+t+t1+t2)/5
        if ave1 + 25 <= ave2:
            move = 'left'
        elif ave1 - 25 >= ave2:
            move = 'right'
        else:
            move = 'still'
        ave2 = ave1
   
    except:
        move = 'pause'
    
    print(move)
   

    
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    image = frame
    lower_red = np.array([20,100,100])
    upper_red = np.array([30,255,255])
    mask = cv2.inRange(image, lower_red, upper_red)  
    coord = cv2.findNonZero(mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    #cv2.imshow('res',res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()