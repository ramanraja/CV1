# Take a snapshot with either the USB camera or the RPi camera
import cv2
import time
import my_imutils
from videostream import VideoStream 

stream = VideoStream()
stream.start()
time.sleep(2.0)

frame= stream.read()
if frame is None:
    print "No camera !"
    stream.stop()
else:    
    frame = my_imutils.resize(frame, 400)
    cv2.putText(frame, "This is frame grabber", (10,10), cv2.FONT_HERSHEY_SIMPLEX,
    0.35, (0, 0, 255), 1)
    
    cv2.imshow("Frame", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    stream.stop()