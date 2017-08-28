# Capture mouse clicks and draw a dot on the image

import numpy as np
import argparse
import cv2
 
file_name = '..\image4\parking.jpg'
points = []

def onMouseClick (event, x, y, flags, param):
	global points  # grab references to the global variable

	if event == cv2.EVENT_LBUTTONUP:
		points.append((x, y))
		cv2.circle(img,(x,y),20,(0,0,255),-1)
		cv2.imshow("On the Dot", img)  # the event handler can update the UI
		
cv2.namedWindow("On the Dot")
cv2.setMouseCallback("On the Dot", onMouseClick)		
img = cv2.imread (file_name)
cv2.imshow("On the Dot", img)		

# Note: there is no infinite loop
cv2.waitKey(0)
print '{0} points were captured'.format(len(points))
print points
cv2.destroyAllWindows()
