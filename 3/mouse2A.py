# Draw a dot on a mouse click, toggling between 2 colors

import numpy as np
import argparse
import cv2
 
file_name = '..\image4\parking.jpg'
window_name = "On the Dot"
green = [0,255,0]
red = [0,0,255]
dotcolor = green
points = []

def onMouseClick (event, x, y, flags, param):
	global points, dotcolor  # grab the references 

	if event == cv2.EVENT_LBUTTONUP:
		points.append((x, y))
		cv2.circle(img,(x,y),20,dotcolor,-1)
		
cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name, onMouseClick)		
img = cv2.imread (file_name)
cv2.imshow(window_name, img)		

while True:
    cv2.imshow(window_name, img)
    key = cv2.waitKey(20)
    if (key==27): break
    if key==116:  # 't' 
        if dotcolor==green:
            dotcolor=red
        else:
            dotcolor=green    

cv2.destroyAllWindows()
