# List of mouse events in cv2

import cv2
 
events = [i for i in dir(cv2) if 'EVENT' in i]
print events 