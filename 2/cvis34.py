# Simple thresholding & inverse thresholding

import cv2
import numpy as np
import argparse

file_name = "bm.jpg"
threshold = 155
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = False, help = "Path to the image")
ap.add_argument("-t", "--thresh", required = False, help = "Threshold")
args = vars(ap.parse_args())
print args
if not args['image']==None: file_name = args['image']
if not args['thresh']==None: threshold = int(args['thresh']) 
print file_name, threshold
    
img = cv2.imread(file_name)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(img, (5, 5), 0)

(T, img2) = cv2.threshold(blurred, threshold, 255, cv2.THRESH_BINARY)
(T, img3) = cv2.threshold(blurred, threshold, 255, cv2.THRESH_BINARY_INV)  

cv2.imshow("Thresh-inverse Thresh", np.hstack([img, img2, img3]))
 
cv2.waitKey(0)
cv2.destroyAllWindows()




