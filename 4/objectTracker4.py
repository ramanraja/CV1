# Object tracking by HSB color, and plot the object's HSV histogram 

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
          
colours = ["B", "G", "R"] # blue line is the hue          
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
        (x,y,w,h) = cv2.boundingRect(cntr[0])
        cv2.rectangle(frame, (x,y),(x+w,y+h), (0, 255, 0), 2)
        copy = frame.copy()[y:y+h, x:x+h]  #  [y1:y2, x1:x2]
        hsv = cv2.split(copy) 
        zipped = zip(hsv, colours)
        plt.figure()
        plt.title('Histograms')

        for (chl, col) in zipped:
            hist = cv2.calcHist([chl], [0], None, [256], [0,256])
            plt.xlim([-5, 260])
            #plt.ylim([0, 10000])  # adjust empirically for each picture
            plt.plot(hist, color=col)

    plt.show()        
    cv2.imshow("Frame", frame)
    
    if cv2.waitKey(0) & 0xff == 27: 
         break
         
print "Bye !"
stream.stop()
time.sleep(2.0)
cv2.destroyAllWindows()
