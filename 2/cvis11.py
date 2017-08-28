# change color of a sub rectangle  

import cv2

x = [0,10,20,30,40,50]
print x[5:2:-1]   # x[5] to x[2], excluding x[2]
print x[2:0:-1]
print x[2::-1]    # x[2] to the beginning of the array

img = cv2.imread('photo.png')
print img.shape

sub = img[0:150, 10:200, ]  # the third dimension is 0:3 
print sub.shape
img[0:150, 10:200, ] =  sub[: , : , 2::-1]
cv2.imshow("My Picture",img)
cv2.waitKey(0)
cv2.destroyAllWindows()