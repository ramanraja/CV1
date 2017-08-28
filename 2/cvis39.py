# Canny edge detection

import cv2
import numpy as np
import argparse

file_name = "bm.jpg"
blur = 5
lower = 30
upper = 150
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",  required = False, help = "Path to the image")
ap.add_argument("-b", "--blur",   required = False, help = "Blurring neighbourhood")
ap.add_argument("-l", "--lower",  required = False, help = "Lower threshold")
ap.add_argument("-u", "--upper",  required = False, help = "Uppder threshold")
args = vars(ap.parse_args())
print args
if not args['image']==None: file_name = args['image']
if not args['blur']==None: blur = int(args['blur']) 
if not args['lower']==None: lower = int(args['lower'])
if not args['upper']==None: upper = int(args['upper'])
print file_name, blur, lower, upper
    
img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
blurred = cv2.GaussianBlur(img, (blur, blur), 0)
edges = cv2.Canny (blurred, 255, lower, upper)
cv2.imshow("Canny Edges", np.hstack([img, edges]))

cv2.waitKey(0)
cv2.destroyAllWindows()




