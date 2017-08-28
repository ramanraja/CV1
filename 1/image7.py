
# coding: utf-8

# In[16]:

from scipy import misc
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[17]:

pic2_name = 'parking4.jpg'
pic1 = misc.imread('parking1.jpg')
print type(pic1)
print pic1.dtype
print pic1.shape  # (height, width, 4) NOTE: for png it is 4, for jpg it is 3
pic2 = misc.imread(pic2_name)
print pic2.shape 


# In[18]:

plt.subplot(1,2,1)
plt.imshow(pic1)
plt.axis('off')
plt.subplot(1,2,2)
plt.imshow(pic2)
plt.axis('off')
plt.show()


# In[19]:

print pic1.shape
print pic2.shape
# pic1.shape - pic2.shape  # error
np.subtract(pic1.shape, pic2.shape)


# In[20]:

minheight = min(pic1.shape[0], pic2.shape[0])
minwidth = min(pic1.shape[1], pic2.shape[1])
print minheight, minwidth


# In[21]:

pic1 = pic1[ :minheight, :minwidth]
pic2 = pic2[ :minheight, :minwidth]
print pic1.shape
print pic2.shape
np.subtract(pic1.shape, pic2.shape)


# In[22]:

dif = pic1 - pic2
print type(dif)
print dif.dtype
print dif.shape
plt.imshow(dif)
plt.axis('off')
plt.show()


# In[23]:

dif = pic2 - pic1
plt.imshow(dif)
plt.axis('off')
plt.show()


# In[24]:

filter_strength = 6
clean = ndimage.median_filter(dif, filter_strength)
plt.imshow(clean)
plt.show()


# In[25]:

# dimensions of a cell
height = clean.shape[0] / 2
width = clean.shape[1] / 3
print height, width


# In[26]:

sub = []
for row in range(2):
    for col in range(3):
        x1 = width*col
        x2 = width*(col+1)
        y1 = height*row
        y2 = height*(row+1)
        sub.append(clean[y1:y2, x1:x2])


# In[27]:

print len(sub)
for i in range(len(sub)):
    print sub[i].shape


# In[28]:

for i in range(len(sub)):
    plt.subplot(2,3,i+1) # i+1 because index 0 is deprecated
    plt.imshow(sub[i])
    plt.axis('off')
plt.show()


# In[29]:

for i in range(len(sub)):
    print sub[i].mean()


# In[30]:

thresh = 10
occupied = []
free = []
for i in range(len(sub)):
    if (sub[i].mean() > thresh):
        occupied.append(i+1)
    else:
        free.append(i+1)
print "occupied: ", occupied
print "free:", free


# In[ ]:



