# Repair the pickle file, if the circle spills out of the picture boundary

import numpy as np
import pickle
import cv2

pickle_file = 'pickle7.p'
retrieved = pickle.load (open(pickle_file, "rt"))
file_name = retrieved['image_file'] 
points = retrieved['markers']
print len(points), ' points marked'

img = cv2.imread (file_name)
my,mx = img.shape[:2]
print "image shape:", my,mx

new_points = []
for i in range(len(points)):
    cx,cy,r = points[i][0:3]
    if(cx-r) < 0: 
        print 'Dropping:', cx,cy,r
        continue
    if(cy-r) < 0:  
        print 'Dropping:', cx,cy,r
        continue
    if(cx+r) > mx:
        print 'Dropping:', cx,cy,r
        continue
    if(cy+r) > my:   
        print 'Dropping:', cx,cy,r
        continue    
    new_points.append(points[i])
    
if len(points) == len(new_points):
    print "All circles are within image boundary"
else:
    print 'Original:{0} points, After repair:{1} points'.format(len(points),len(new_points))
    annotated_image = {'image_file': file_name, 'markers': new_points} 
    new_pickle_file = 'Repaired_' + pickle_file
    pickle.dump (annotated_image, open(new_pickle_file, "wt"))
    print 'Pickle file saved as: ', new_pickle_file
 

