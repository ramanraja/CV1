# Take a snapshot, cut out the faces and save in individual files

import cv2
import time
import my_imutils
from videostream import VideoStream 

#Load a cascade file for detecting faces
face_cascade = cv2.CascadeClassifier('../XML/haarcascades/haarcascade_frontalface_alt.xml')

stream = VideoStream()
stream.start()
time.sleep(2.0)
frame = stream.read()
if frame is None:
    print "No camera !"
    raise SystemExit(1)   
         
for i in range(10):
    frame = stream.read()
    frame = my_imutils.resize(frame, 480)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    nfaces = len(faces)
    print "Found "+str(nfaces)+" face(s)"
 
    j = 0
    for (x,y,w,h) in faces:
          cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)  
          copy = frame.copy()[y:y+h, x:x+h]  #  [y1:y2, x1:x2]  
          cv2.imwrite("face{0}_{1}.jpg".format(i,j), copy)
          j += 1
          
    cv2.imshow("Face{0}".format(j), frame)
    print "Press any key... (Esc to quit)"
    if cv2.waitKey(0) & 0xff == 27: break
    
stream.stop()    
time.sleep(2)  # need time to join the thread; otherwise it hangs
cv2.destroyAllWindows()
print "Bye !"