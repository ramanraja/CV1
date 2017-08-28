# List of mouse/keyboard events in cv2

import cv2
 
features = dir(cv2)
print len(features)
for f in features:
    if 'EVENT' in f:
        print f
     
 