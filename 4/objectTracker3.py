# Object tracking by HSB color, mainly the hue 

import cv2
import time
import numpy as np
import matplotlib.pyplot as plt
import my_imutils
from videostream import VideoStream 

# note: it is in H,S,V order
#Lower = np.array([90, 0, 0], dtype = "uint8")
#Upper = np.array([120, 255, 255], dtype = "uint8")
Lower = np.array([90, 80, 80], dtype = "uint8")
Upper = np.array([120, 255, 255], dtype = "uint8")

source = 0  # camera
stream = VideoStream(src=source)
stream.start()
time.sleep(2.0)
frame = stream.read()
if frame is None:
    print "No camera !"
    raise SystemExit(1)   
          
while(True): 
    frame = stream.read()
    frame = my_imutils.resize(frame, 480)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blue = cv2.inRange(frame, Lower, Upper)
    blue = cv2.GaussianBlur(blue, (3, 3), 0)
    # finding contours destroys the original image, so make a copy first
    (junk_img, contours, hierarchy) = cv2.findContours(blue.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) > 0:
        cntr = sorted(contours, key = cv2.contourArea, reverse = True)
        #cv2.drawContours(frame, cntr, -1, (0, 255, 0), 2)
        #rect = np.int32(cv2.BoxPoints(cv2.minAreaRect(cntr)))
        #cv2.drawContours(frame, [rect], -1, (0, 255, 0), 2)
        (x,y,w,h) = cv2.boundingRect(cntr[0])
        cv2.rectangle(frame, (x,y),(x+w,y+h), (0, 255, 0), 2)

    
    cv2.imshow("Frame", frame)
    if cv2.waitKey(0) & 0xff == 27: 
         break
         
print "Bye !"
stream.stop()
time.sleep(2.0)
cv2.destroyAllWindows()
