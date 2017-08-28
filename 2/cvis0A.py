# color channel reversal
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('bm.jpg')
print img.shape
# translate from bgr to rgb format
img[:,:,:] = img[:,:,(2,1,0)]  
plt.imshow(img) # color corrected
plt.show()


