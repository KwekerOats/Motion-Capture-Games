import cv2
import numpy as numpy

device = cv2.VideoCapture(0)
while True:
  ret, frame = device.read()
  hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

  lower_range = np.array([110,50,50])
  upper_range = np.array([130,255,255])

  mask = cv2.inRange(hsv, lower_range,upper_range)
  cv2.imshow('Frame',frame)

  result = cv2.bitwise_and(frame,frame,mask=mask)
  cv2.imshow('Result',result)


  if cv2.waiKey(1) == 27:
    break

device.release()
cv2.destroyAllWindows()
