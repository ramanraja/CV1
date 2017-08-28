# Simple inverse threshold & apply it as a mask

import cv2
import numpy as np
import argparse

file_name = "bm.jpg"
threshold = 155
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",  required = False, help = "Path to the image")
ap.add_argument("-t", "--thresh", required = False, help = "Threshold")
args = vars(ap.parse_args())
print args
if not args['image']==None: file_name = args['image']
if not args['thresh']==None: threshold = int(args['thresh']) 
print file_name, threshold
    
img = cv2.imread(file_name)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(img, (5, 5), 0)

(T, the_mask) = cv2.threshold(blurred, threshold, 255, cv2.THRESH_BINARY_INV) 
print 'T=', T 
# masked = cv2.bitwise_and(img, img, the_mask) # Wrong: the third argument MUST be named
masked = cv2.bitwise_and(img, img, mask=the_mask)

cv2.imshow("Thresholded", np.hstack([img, the_mask, masked]))
 
cv2.waitKey(0)
cv2.destroyAllWindows()




