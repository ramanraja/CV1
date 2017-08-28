# Take a series of snapshots with USB/ RPi camera and save

import cv2
import time
import my_imutils
from videostream import VideoStream 

stream = VideoStream()
stream.start()
time.sleep(2.0)
    
for i in range(3):
    frame= stream.read()
    if frame is None:
        print "No camera !"
        break
    else:    
        frame = my_imutils.resize(frame, 400)
        cv2.putText(frame, "This is frame grabber", (10,10), cv2.FONT_HERSHEY_SIMPLEX,
        0.35, (0, 0, 255), 1)
        cv2.imshow("Frame", frame)
        cv2.imwrite("face{0}.jpg".format(i), frame)
    print "Press any key... (Esc to quit)"
    if cv2.waitKey(0) & 0xff == 27: break
    
stream.stop()    
time.sleep(2)  # need time to join the thread; otherwise it hangs
cv2.destroyAllWindows()
print "Bye !"