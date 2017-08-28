# Cut off circular zones from an image and get masked B,G,R histograms; Classify with SVM classifier.  

import matplotlib.pyplot as plt
from sklearn import svm
import numpy as np
import pickle
import os.path
import argparse
import cv2

def refresh ():
    global img
    img = original_img.copy()
    for i in range(len(points)):
        pt = (points[i][0], points[i][1])
        r = points[i][2]
        dc = dotcolors[points[i][3]]
        if pred[i]==0:
            cv2.circle(img,pt, r, dc,2)
            pt = (points[i][0]-4, points[i][1]+4)
            cv2.putText(img, "F", pt, font, 0.5, (255,255,255),2)
        elif pred[i]==1:
            cv2.circle(img,pt, r, dc,-1)
    cv2.imshow(window_name, img)  
    
def getFrame((cx,cy,r)):
    x1 = cx-r
    x2 = cx+r
    y1 = cy-r
    y2 = cy+r
    assert (x1>=0 and x2>=0 and y1>=0 and y2>=0), "Circle spills out of the picture frame:{0},{0},{2}".format (cx,cy,r)
    subimg = img[y1:y2, x1:x2].copy()
    return subimg
#----------------------------------------------------------------

window_name = 'Annotated'
font = cv2.FONT_HERSHEY_SIMPLEX
dotcolors = ([0,255,0], [0,0,255], [255,0,0])
pickle_file = 'pickle4.p' #  
 
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--pickle",   required = False, help = "Pickle file name")
args = vars(ap.parse_args())
print args
if not args['pickle']==None: pickle_file = args['pickle'] 
print pickle_file

retrieved = pickle.load (open(pickle_file, 'rt'))
file_name = retrieved['image_file'] 
points = retrieved['markers']
print len(points), ' markers found'

original_img = cv2.imread (file_name)
print original_img.shape
assert (original_img is not None), 'File not found'
img = original_img.copy()
#cv2.imshow(window_name, img)		
#refresh()

num_bins = 16

da = []
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
    histb = histb.flatten()   # make it n length vector
    histg = histg.flatten()
    histr = histr.flatten()
    
    features = []
    features.extend(histb)
    features.extend(histg)
    features.extend(histr)
    features.append(points[i][3])  # dot color/prediction outcome  
    
    features = np.array(features)
    da.append(features)
#--------------------------------------------------------------------
print type(da) 
da = np.array(da)
print da.shape

classifier = svm.SVC(kernel='linear', C = 1.0)
classifier.fit(da[: ,:48], da[:,-1])

pred = classifier.predict(da[: ,:48])
print pred
print da[:, -1]
print '-'*15
print np.subtract(da[:,-1], pred)
print 'Number of misclassifications:', int(sum(np.subtract(da[:,-1], pred)))

refresh()
cv2.waitKey(0)
cv2.destroyAllWindows()
    


