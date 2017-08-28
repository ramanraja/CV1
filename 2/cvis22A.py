# Resize an image, preserve aspect ratio

import cv2
     
img = cv2.imread('bm.jpg')
height = img.shape[0]
width = img.shape[1]
magnification = 3
newsize = (int(magnification*width), int(magnification*height))

img2 = cv2.resize(img, newsize, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized", img2)
cv2.waitKey(4000)
cv2.destroyAllWindows()



