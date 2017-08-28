# Multiple thresholding methods on a noisy/filtered image: demo

import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse

file_name = 'noisy2.png'
blur = 5

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",  required = False, help = "Path to the image")
ap.add_argument("-b", "--blur",  required = False, help = "Blurring neighbourhood")
args = vars(ap.parse_args())
print args
if not args['image']==None: file_name = args['image']
if not args['blur']==None: blur = int(args['blur']) 
print file_name, blur 
    
img = cv2.imread (file_name, 0) # 0 to read it as gray scale image
# global thresholding
ret1,th1 = cv2.threshold (img,127,255,cv2.THRESH_BINARY)
   
# Otsu's thresholding
ret2,th2 = cv2.threshold (img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur (img,(blur, blur),0)
ret3,th3 = cv2.threshold (blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
# plot all the images and their histograms
images = [img, 0, th1, img, 0, th2, blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
    'Original Noisy Image','Histogram',"Otsu's Thresholding",
    'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

for i in xrange(3):
     plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
     plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
     plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
     plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
     plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
     plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()