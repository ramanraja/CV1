# Mark dot positions on a picture, pickle to file, reload and edit

import numpy as np
import pickle
import os.path
import argparse
import cv2

#-------------------------------------------------------

def onMouseClick (event, x, y, flags, param):
	global points, dirty                   # external variables to be modified 
	dirty = True
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

dirty = False
window_name = "On the Dot"
dotcolors = ([0,255,0], [0,0,255])
currentcolor = 0
rad = 20
file_name = 'parking.jpg'
pickle_file = 'pickle1.p'
points = []

if os.path.isfile(pickle_file):
    retrieved = pickle.load (open(pickle_file, "rb"))
    file_name = retrieved['image_file'] 
    points = retrieved['markers']

cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name, onMouseClick)		
original_img = cv2.imread (file_name)
assert (original_img is not None), 'File not found'
img = original_img.copy()
cv2.imshow(window_name, img)		
refresh()

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

if dirty:
    annotated_image = {'image_file': file_name, 'markers':points} 
    pickle.dump (annotated_image, open(pickle_file, "wb"))

cv2.destroyAllWindows()

