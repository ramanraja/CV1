# Take a zone-marked file; split it to multiple images; mask out the exterior of the circles

import numpy as np
import pickle
import os.path
import argparse
import cv2

def refresh():
    global img
    #img = original_img.copy()
    for i in range (len(points)):
        cv2.circle (img,(points[i][0], points[i][1]), points[i][2], dotcolors[points[i][3]],2)
    cv2.imshow (window_name, img) 
    
def getFrame((cx,cy,r)):
    x1 = cx-r
    x2 = cx+r
    y1 = cy-r
    y2 = cy+r
    assert (x1>=0 and x2>=0 and y1>=0 and y2>=0), "Circle spills out of the picture frame:{0},{0},{2}".format (cx,cy,r)
    subimg = img[y1:y2, x1:x2].copy()
    mask = np.zeros (subimg.shape[:2], dtype='uint8')
    cv2.circle (mask,(r,r),r,255,-1)
    subimg = cv2.bitwise_and (subimg, subimg, mask=mask)
    return subimg

dotcolors = ([0,255,0], [0,0,255], [255,0,0])
pickle_file = 'Repaired_pickle1.p'
window_name = "Annotated"
retrieved = pickle.load (open(pickle_file, "rt"))
file_name = retrieved['image_file'] 
points = retrieved['markers']
print len(points), ' points marked'
#print points
print points[49:51]

original_img = cv2.imread (file_name)
print original_img.shape
assert (original_img is not None), 'File not found'
img = original_img.copy()
refresh()  # just for testing
cv2.imshow(window_name, img)		

'''
fr1 = getFrame((150,150,148))
cv2.imshow("frame1", fr1)
fr2 = getFrame((150,150,100))
cv2.imshow("frame2", fr2)
fr2 = getFrame((150,150,200)) # assertion failure
cv2.imshow("frame2", fr2)
'''

counter = range(0,len(points),10)
print counter
for i in counter: 
    print i
    fr = getFrame(points[i][0:3])
    print fr.shape
    cv2.imshow("frame{0}".format(i), fr)
 
cv2.waitKey(0)
cv2.destroyAllWindows()

