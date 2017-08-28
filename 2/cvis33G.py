# Bilateral blur, fully configurable
# preserves edges, while still reducing noise
# only pixels with similar intensity are included in the computation of blur

import cv2
import numpy as np
import argparse

file_name = "bm.jpg"
blur = 7
sigma1 = 21
sigma2 = 21

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",  required = False, help = "Path to the image")
ap.add_argument("-b", "--blur",   required = False, help = "Blurring neighbourhood")
ap.add_argument("-s1", "--sigma1",  required = False, help = "Space Sigma neighbourhood")
ap.add_argument("-s2", "--sigma2",  required = False, help = "Color Sigma neighbourhood")

args = vars(ap.parse_args())
print args
if not args['image']==None: file_name = args['image']
if not args['blur']==None: blur = int(args['blur']) 
if not args['sigma1']==None: lower = int(args['sigma1'])
if not args['sigma2']==None: upper = int(args['sigma2'])
print file_name, blur, sigma1, sigma2
    
img = cv2.imread(file_name) #, cv2.IMREAD_GRAYSCALE)
assert (img is not None), 'File not found'
print img.shape

# parameters: image, neighbourhood diameter, color sigma, space sigma-subject to similarity of color
blurred = cv2.bilateralFilter(img, blur, sigma1, sigma2) 

cv2.imshow("Original", img)
cv2.imshow("Bilateral Blur", blurred)
 
cv2.waitKey(0)
cv2.destroyAllWindows()




