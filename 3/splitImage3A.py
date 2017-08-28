# Cut off marked circular zones from an image and plot B,G,R histograms; Now applying the mask within calcHist call

import matplotlib.pyplot as plt
import numpy as np
import pickle
import os.path
import argparse
import cv2

def refresh():
    global img
    #img = original_img.copy()
    for i in range (len(points)):
        cv2.circle (img,(points[i][0], points[i][1]), points[i][2], dotcolors[points[i][3]],2)
    cv2.imshow (window_name, img) 
    
def getFrame((cx,cy,r)):
    x1 = cx-r
    x2 = cx+r
    y1 = cy-r
    y2 = cy+r
    assert (x1>=0 and x2>=0 and y1>=0 and y2>=0), "Circle spills out of the picture frame:{0},{0},{2}".format (cx,cy,r)
    subimg = img[y1:y2, x1:x2].copy()
    #mask = np.zeros (subimg.shape[:2], dtype='uint8')
    #cv2.circle (mask,(r,r),r,255,-1)
    #subimg = cv2.bitwise_and (subimg, subimg, mask=mask)
    return subimg

dotcolors = ([0,255,0], [0,0,255], [255,0,0])
pickle_file = 'pickle2.p'  #'Repaired_pickle1.p'
window_name = 'Annotated'
retrieved = pickle.load (open(pickle_file, 'rt'))
file_name = retrieved['image_file'] 
points = retrieved['markers']
print len(points), ' markers found'

original_img = cv2.imread (file_name)
print original_img.shape
assert (original_img is not None), 'File not found'
img = original_img.copy()
refresh()  # just for testing
cv2.imshow(window_name, img)		

plt.figure()
plt.title('Histograms')

for i in range(len(points)): 
    frame = getFrame(points[i][0:3])
    mask = np.zeros (frame.shape[:2], dtype='uint8')
    r = points[i][2]
    cv2.circle (mask,(r,r),r,255,-1)
    b,g,r = cv2.split(frame)
    histb = cv2.calcHist([b], [0], mask, [64], [0,256])
    histg = cv2.calcHist([g], [0], mask, [64], [0,256])
    histr = cv2.calcHist([r], [0], mask, [64], [0,256])
    plt.subplot(2,2,i+1)
    plt.xlim([-1, 65])
    #plt.ylim([0, 10000])  # adjust empirically for each picture
    plt.plot(histb, color='b')
    plt.plot(histg, color='g')
    plt.plot(histr, color='r')
plt.show()

