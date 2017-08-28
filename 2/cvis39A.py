# Canny edge detection; resize larger images before displaying

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
blur = 5
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

#img = shrink(img)
#print img.shape

if resize=='Y' or resize=='y':
    cv2.imshow("Canny Edges", np.hstack([shrink(img), shrink(edges)]))
else:
    cv2.imshow("Original", img)
    cv2.imshow("Canny Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()




