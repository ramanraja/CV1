# Color histogram of the 3 channels - simplified for clarity

import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

file_name = "jurassic.jpg"
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = False, help = "Path to the image")
args = vars(ap.parse_args())
print args
if args['image'] is not None:
    file_name = args['image']
print file_name
    
img = cv2.imread(file_name)
assert (img is not None), "File not found"
print img.shape
cv2.imshow("Image", img)

channels = cv2.split(img)
print "channels[0] shape:", channels[0].shape
(b,g,r) = cv2.split(img)

histb = cv2.calcHist([b], [0], None, [32], [0,256])
print "Histogram shape:", histb.shape   #
histg = cv2.calcHist([g], [0], None, [32], [0,256])
histr = cv2.calcHist([r], [0], None, [32], [0,256])

plt.figure()
plt.title('Histograms')
plt.xlim([-1, 33])
#plt.ylim([0, 10000])  # adjust empirically for each picture
plt.plot(histb, color='b')
plt.plot(histg, color='g')
plt.plot(histr, color='r')
plt.show()

 




