# difference between numpy array coordinates and drawing coordinates.

import cv2

red = [0,0,255]
img = cv2.imread('photo.png')
print img.size   # byte size; slightly larger than the file size
print img.shape  # y,x  or rows, cols

img2 = img[30:150, 0:200] # numpy array coordinates: [y1 to y2, x1 to x2]
cv2.rectangle(img, (0,30), (200,150), red, 3)  # drawing coordinates: (x1,y1), (x2,y2)

cv2.imshow("Original", img)
cv2.imshow("Cut", img2) # what you drew on img is visible on img2 also !

cv2.waitKey(0)
cv2.destroyAllWindows()