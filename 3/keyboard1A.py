# Capture and print keyboard strokes

import cv2
import numpy as np

img = np.zeros((100,100), dtype='uint8')  # a dummy window is needed
cv2.imshow("Dummy", img) 
while True:
    key = cv2.waitKey(20)
    # -1 if there is no key press
    if (key > 0): 
        print key, ":", unichr(key)   
    if (key==27): break
    if (key==ord('r')): print 'R pressed'
    else:
       if (key==ord('s')): print 'S pressed'
        
cv2.destroyAllWindows()    