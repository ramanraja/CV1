# Take a snapshot/read a directory of still images, cut out the faces and save them as individual files

import cv2
import time
import my_imutils
import paths  # src file pulled from imutils
from videostream import VideoStream 
import argparse

#-----------------------------------------------------------------------------
def save_faces(i, frame):
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
          
    cv2.imshow("Frame", frame)
    print "Press any key... (Esc to quit)"
    if cv2.waitKey(0) & 0xff == 27: 
        return False
    return True
#-----------------------------------------------------------------------------  
  
dir_name = None
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dir",  required = False, help = "Path to the images directory")
args = vars(ap.parse_args())
if not args['dir']==None: dir_name = args['dir']
print dir_name

#Load a cascade file for detecting faces
face_cascade = cv2.CascadeClassifier('../XML/haarcascades/haarcascade_frontalface_alt.xml')
i = 0  
if dir_name is None:
    stream = VideoStream()
    stream.start()
    time.sleep(2.0)
    frame = stream.read()
    if frame is None:
        print "No camera !"
        raise SystemExit(1)         
    while(True):
        i += 1    
        frame = stream.read()
        if not save_faces(i, frame): 
            stream.stop()    
            time.sleep(2)  # avoid deamon thread hanging
            break
else:
    for file_name in paths.list_images(dir_name):
        i += 1
        frame = cv2.imread(file_name)
        if not save_faces(i, frame): 
            break

cv2.destroyAllWindows()
print "Bye !"