# Three dimensional histogram 

import cv2
import numpy as np
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

hist = cv2.calcHist([b,g,r], [0,1,2], None, [8,8,8], [0,256, 0,256, 0,256])
flat = hist.flatten()
print hist.shape
print flat.shape 
print flat.shape[0] 

print '-------------------------------'
hist = cv2.calcHist([b,g,r], [0,1,2], None, [3,3,3], [0,256, 0,256, 0,256])
print hist.shape
flat = hist.flatten()
print flat.shape 

print '-----------------'
print hist

