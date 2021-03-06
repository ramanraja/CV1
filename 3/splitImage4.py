# Cut off circular zones from an image and get masked B,G,R histograms; Save the histograms to a CSV file. Take input and output file names from the command line

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
    return subimg

window_name = 'Annotated'
dotcolors = ([0,255,0], [0,0,255], [255,0,0])
pickle_file = 'pickle.p' 
out_file = 'features.csv'

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--outfile",  required = False, help = "Output CSV file")
ap.add_argument("-p", "--pickle",   required = False, help = "Pickle file name")
args = vars(ap.parse_args())
print args
if not args['outfile']==None: out_file = args['outfile']
if not args['pickle']==None: pickle_file = args['pickle'] 
print out_file, pickle_file

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

feature_file = open(out_file, 'wt') 
plt.figure()
plt.title('Sample Histograms')

num_bins = 16

for i in range(len(points)): 
    frame = getFrame(points[i][0:3])
    mask = np.zeros (frame.shape[:2], dtype='uint8')
    r = points[i][2]
    cv2.circle (mask,(r,r),r,255,-1)
    
    b,g,r = cv2.split(frame)
    histb = cv2.calcHist([b], [0], mask, [num_bins], [0,256])
    histg = cv2.calcHist([g], [0], mask, [num_bins], [0,256])
    histr = cv2.calcHist([r], [0], mask, [num_bins], [0,256])
    #print histb.shape        # nx1 matrix
    histb = histb.flatten()  # make it n length vector
    histg = histg.flatten()
    histr = histr.flatten()
    
    features = []
    features.extend(histb)
    features.extend(histg)
    features.extend(histr)
    features.append(points[i][3])  # dot color/prediction outcome  
    
    fstring = ','.join(str(num) for num in features)
    feature_file.write(fstring)
    feature_file.write('\n')
    
    if i<9:
        plt.subplot(3,3,i+1)
        plt.xlim([-1, num_bins+1])
        #plt.ylim([0, 10000])  # adjust empirically for each picture
        plt.plot(histb, color='b')
        plt.plot(histg, color='g')
        plt.plot(histr, color='r')
feature_file.close()
print 'Features file saved as:', out_file
plt.show()

