# Color histograms of a camera image

import cv2
import time
import numpy as np
import matplotlib.pyplot as plt
import my_imutils
from videostream import VideoStream 

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
    cv2.imshow("Frame", frame)
    chls = cv2.split(frame)
    colours = ["B", "G", "R"]
    zipped = zip(chls, colours)
    plt.figure()
    plt.title('Histograms')
    for (chl, col) in zipped:
        hist = cv2.calcHist([chl], [0], None, [256], [0,256])
        plt.xlim([-5, 260])
        #plt.ylim([0, 10000])  # adjust empirically for each picture
        plt.plot(hist, color=col)
    plt.show()
    if cv2.waitKey(0) & 0xff == 27: 
         break

stream.stop()
time.sleep(2.0)
cv2.destroyAllWindows()
print "Bye !"