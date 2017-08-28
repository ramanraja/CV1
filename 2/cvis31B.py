# Two dimensional histograms

import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

file_name = "redcar.png"
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = False, help = "Path to the image")
args = vars(ap.parse_args())
print args
if args['image']==None:
    args['image'] = file_name
    
img = cv2.imread(args['image'])
print img.shape
(b,g,r) = cv2.split(img)

plt.figure()
plt.title('2D Histogram')

hist = cv2.calcHist([b,g], [0,1], None, [32,32], [0,256, 0,256])
plt.xlim([-2, 34])
#plt.ylim([0, 10000])  # adjust empirically for each picture
fig = plt.imshow(hist, interpolation='nearest')
plt.colorbar(fig)

plt.show()
 
 




