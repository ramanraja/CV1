# Adaptive Gaussian thresholding

import cv2
import numpy as np
import argparse

file_name = "bm.jpg"
blur = 5
neighbourhood = 15
cparam = 3
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",  required = False, help = "Path to the image")
ap.add_argument("-b", "--blur",  required = False, help = "Blurring neighbourhood")
ap.add_argument("-n", "--nbd", required = False, help = "Neighbourhood size (must be odd, >1")
ap.add_argument("-c", "--C", required = False, help = "C parameter")
args = vars(ap.parse_args())
print args
if not args['image']==None: file_name = args['image']
if not args['blur']==None: blur = int(args['blur']) 
if not args['nbd']==None: neighbourhood = int(args['nbd']) 
if not args['C']==None: cparam = int(args['C']) 
print file_name, neighbourhood, cparam
    
img = cv2.imread(file_name)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(img, (blur, blur), 0)

the_mask = cv2.adaptiveThreshold (blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, neighbourhood, cparam) 
# masked = cv2.bitwise_and(img, img, the_mask) # Wrong: the third argument MUST be named
masked = cv2.bitwise_and(img, img, mask=the_mask)

cv2.imshow("Adaptive Gaussian Thresholded", np.hstack([img, the_mask, masked]))
 
cv2.waitKey(0)
cv2.destroyAllWindows()




