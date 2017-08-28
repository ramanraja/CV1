# Draw dots on mouse click, change color, size or delete

import numpy as np
import argparse
import cv2

#-------------------------------------------------------

def onMouseClick (event, x, y, flags, param):
	global points # grab the variable to be modified 
	if event == cv2.EVENT_LBUTTONUP:
		points.append((x, y, rad, currentcolor))
		cv2.circle(img,(x,y),rad, dotcolors[currentcolor],2)
#-------------------------------------------------------

def refresh ():
    global img
    img = original_img.copy()
    for i in range(len(points)):
        cv2.circle(img,(points[i][0], points[i][1]), points[i][2], dotcolors[points[i][3]],2)
    cv2.imshow(window_name, img)  
#-------------------------------------------------------
     
file_name = '..\image4\parking.jpg'
window_name = "On the Dot"
dotcolors = ([0,255,0], [0,0,255])
currentcolor = 0
rad = 20
points = []

cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name, onMouseClick)		
original_img = cv2.imread (file_name)
img = original_img.copy()
cv2.imshow(window_name, img)		

while True:
    cv2.imshow(window_name, img)
    key = cv2.waitKey(20)
    if (key < 0): continue
    if (key==27): break
    if key==ord('t'):   
        currentcolor = (currentcolor+1)%2
    elif key==ord('d'):
        if(len(points) > 0): 
            points = points[:-1]
            refresh() 
    elif key==ord('s'):
        rad -= 2
    elif key==ord('b'):
        rad += 2

print points
print len(points), " points marked"    

f = open('outfile.txt', 'wt')                
f.write(file_name +'\n')
for i in range(len(points)):
    f.write('{0},{1},{2},{3}\n'.format(points[i][0],points[i][1],points[i][2],points[i][3]))
f.close()
cv2.destroyAllWindows()

