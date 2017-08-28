# Capture and print keyboard strokes

import cv2
import numpy as np

img = np.zeros((100,100), dtype='uint8')  # dummy window is needed
cv2.imshow("Dummy", img) 
while True:
    key = cv2.waitKey(20)
    if (key > 0): print key  # -1 if there is no key press
    if (key==27): break
        
cv2.destroyAllWindows()    