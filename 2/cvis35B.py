#  Otsu + Binary thresholding using cv2

import cv2
import numpy as np
import argparse

file_name = "bm.jpg"
blur = 5

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",  required = False, help = "Path to the image")
ap.add_argument("-b", "--blur",  required = False, help = "Blurring neighbourhood")

args = vars(ap.parse_args())
print args
if not args['image']==None: file_name = args['image']
if not args['blur']==None: blur = int(args['blur']) 
print file_name, blur 
    
img = cv2.imread(file_name)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(img, (blur, blur), 0)

T, the_mask = cv2.threshold(blurred, 0, 255, cv2.THRESH_OTSU+cv2.THRESH_BINARY) 
print "Otsu's threshold: %d" % (T)
#masked = cv2.bitwise_and(img, img, the_mask) # Wrong: the third argument MUST be named
masked = cv2.bitwise_and(img, img, mask=the_mask)

cv2.imshow("Otsu Thresholded", np.hstack([img, the_mask, masked]))
 
cv2.waitKey(0)
cv2.destroyAllWindows()




