# Detect contours and mask out the subshapes (coins) alone, deleting the background

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
    
original_img = cv2.imread(file_name) # color image is needed later
img = cv2.cvtColor (original_img, cv2.COLOR_BGR2GRAY)
print img.shape

blurred = cv2.GaussianBlur(img, (blur, blur), 0) # this parameter needs careful tuning

edges = cv2.Canny (blurred, 255, lower, upper)
print edges.shape
 
# ** Finding contours is destructive to the image **
# Make a copy before fining contours
(junk_img, contours, hierarchy) = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print "%d contours were found" %len(contours)

for (i, contour) in enumerate(contours):
    (x,y,w,h) = cv2.boundingRect(contour)
    ((cx,cy),r) = cv2.minEnclosingCircle(contour)
    mask_canvas = np.zeros(original_img.shape[0:2], dtype='uint8')
    cv2.circle(mask_canvas, (int(cx), int(cy)), int(r), 255,-1)
    mask = mask_canvas[y:y+h, x:x+w]
    subimg = original_img[y:y+h, x:x+w]
    title = "Masked {0}".format(i+1)
    cv2.imshow(title, cv2.bitwise_and(subimg, subimg, mask=mask))

cv2.waitKey(0)
cv2.destroyAllWindows()




