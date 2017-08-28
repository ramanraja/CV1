# Capture mouse clicks and draw a circle on an image

import numpy as np
import argparse
import cv2
 
# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img,(x,y),50,(0,0,255),2)

# Create a black image, a window and bind the function to window
img = cv2.imread('img1.jpg')
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
   cv2.imshow('image',img)
   if cv2.waitKey(20) & 0xFF == 27:
         break
cv2.destroyAllWindows()