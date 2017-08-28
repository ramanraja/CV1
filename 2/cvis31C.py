# Two dimensional histograms - all combinations

import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

file_name = "group.jpg"
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = False, help = "Path to the image")
args = vars(ap.parse_args())
print args
if args['image']==None:
    args['image'] = file_name
    
img = cv2.imread(args['image'])
print img.shape
(b,g,r) = cv2.split(img)

fig = plt.figure()
#plt.title('2D Histogram')

hist = cv2.calcHist([b,g], [0,1], None, [32,32], [0,256, 0,256])
subplt = fig.add_subplot(1,3,1)
subplt.set_xlim([-1, 33])
subplt.set_title("B-G")
im = subplt.imshow(hist, interpolation='nearest')

hist = cv2.calcHist([g,r], [0,1], None, [32,32], [0,256, 0,256])
subplt = fig.add_subplot(1,3,2)
subplt.set_xlim([-1, 33])
subplt.set_title("G-R")
im = subplt.imshow(hist, interpolation='nearest')

hist = cv2.calcHist([r,b], [0,1], None, [32,32], [0,256, 0,256])
subplt = fig.add_subplot(1,3,3)
subplt.set_xlim([-1, 33])
subplt.set_title("R-B")
im = subplt.imshow(hist, interpolation='nearest')
#plt.colorbar(im)

plt.show()
 
 




