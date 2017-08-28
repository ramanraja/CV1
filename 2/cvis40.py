# Contour detection using Canny edge detection; experiments with the API

import cv2
import numpy as np
import argparse

def shrink(image, maxWidth=300):
    w = image.shape[1]
    h = image.shape[0]
    if w <= maxWidth:
        return image
    newHeight = int(float(maxWidth)*h/w+0.5)
    return cv2.resize(image, (maxWidth, newHeight))

file_name = "bm.jpg"
blur = 9
lower = 30
upper = 150
resize = 'N'
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",  required = False, help = "Path to the image")
ap.add_argument("-b", "--blur",   required = False, help = "Blurring neighbourhood")
ap.add_argument("-l", "--lower",  required = False, help = "Lower threshold")
ap.add_argument("-u", "--upper",  required = False, help = "Uppder threshold")
ap.add_argument("-r", "--resize", required = False, help = "Resize display Y/N")
args = vars(ap.parse_args())
print args
if not args['image']==None: file_name = args['image']
if not args['blur']==None: blur = int(args['blur']) 
if not args['lower']==None: lower = int(args['lower'])
if not args['upper']==None: upper = int(args['upper'])
if not args['resize']==None: resize = args['resize']

print file_name, blur, lower, upper, resize
    
img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
print img.shape

blurred = cv2.GaussianBlur(img, (blur, blur), 0)

edges = cv2.Canny (blurred, 255, lower, upper)
cv2.imshow("Original Edges", edges)

(img2, contours, hierarchy) = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print "%d countours were found" %len(contours)
cv2.imshow("Destroyed Edges", edges) # finding contours destroys the image
cv2.imshow("Returned image", img2)

edges = cv2.Canny (blurred, 255, lower, upper) # regenerate edges
(img2, contours, hierarchy) = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("Copy() saves Edges", edges) 

img2 = cv2.imread(file_name) # bring back the color image
cv2.imshow("Original Image", img2)

# Draw all contours with -1    
# cv2.drawContours(img2, contours, -1, (0, 255, 0), 4)

# The contours appear in any order !
colors = [(255,0,0), (0,255,0), (0,0,255), (0,255,255), (0,255,255), (0,255,255), (0,255,255), (0,255,255), (0,255,255)]
# Aliter: draw by contour number
for i in range(len(contours)):
    cv2.drawContours(img2, contours, i, colors[i], 2)

cv2.imshow("Image with contours", img2) # original image permanently got the contours on it

cv2.waitKey(0)
cv2.destroyAllWindows()




