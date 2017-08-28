# Adjust amera parameters like resolution, frame rate etc.
# http://stackoverflow.com/questions/11420748/setting-camera-parameters-in-opencv-python

import cv2
camera = cv2.VideoCapture(0)

# open the camera config dialog
camera.set(cv2.CAP_PROP_SETTINGS, 0);
 
while True:
    (grabbed, frame) = camera.read()
    cv2.imshow("Camera", frame)
    key = cv2.waitKey(10) # when idle, 255 or -1
    if key > 0: break
 
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)

while True:
    (grabbed, frame) = camera.read()
    cv2.imshow("Camera", frame)
    key = cv2.waitKey(10)  
    if key > 0: break
    
camera.set(cv2.CAP_PROP_FPS , 3)

while True:
    (grabbed, frame) = camera.read()
    cv2.imshow("Camera", frame)
    key = cv2.waitKey(10)  
    if key > 0: break
        
camera.release()
cv2.destroyAllWindows()	
