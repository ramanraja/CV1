
# coding: utf-8

# In[25]:

from scipy import misc
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
#% matplotlib inline


# In[26]:

pic2_name = 'parking100_3.jpg'
pic1 = misc.imread('parking100_1.jpg')
print type(pic1)
print pic1.dtype
print pic1.shape  # (height, width, 4) NOTE: for png it is 4, for jpg it is 3
pic2 = misc.imread(pic2_name)
print pic2.shape 


# In[27]:

print pic1.shape
print pic2.shape
# pic1.shape - pic2.shape  # error
np.subtract(pic1.shape, pic2.shape)


# In[28]:

minheight = min(pic1.shape[0], pic2.shape[0])
minwidth = min(pic1.shape[1], pic2.shape[1])
print minheight, minwidth


# In[29]:

offset1 = 0  # XL header and side bar, if present
offset2 = 0
pic1 = pic1[offset1:minheight, offset2:minwidth]
pic2 = pic2[offset1:minheight, offset2:minwidth]
print pic1.shape
print pic2.shape
print np.subtract(pic1.shape, pic2.shape)


# In[30]:

# negative difference - this has better contrast
dif = pic1 - pic2
print type(dif)
print dif.dtype
print dif.shape


# In[31]:

# positive difference - less contrast
dif2 = pic2 - pic1


# In[32]:

filter_strength = 6
clean = ndimage.median_filter(dif, filter_strength)


# In[33]:

# dimensions of a cell
height = clean.shape[0] / 10
width = clean.shape[1] / 10
print height, width


# In[34]:

sub = []
for row in range(10):
    for col in range(10):
        x1 = width*col
        x2 = width*(col+1)
        y1 = height*row
        y2 = height*(row+1)
        sub.append(clean[y1:y2, x1:x2])


# In[35]:

print len(sub)
#for i in range(len(sub)):
#    print sub[i].shape
print sub[0].shape


# In[ ]:




# In[36]:

mean_intensity = []
for i in range(len(sub)):
    mean_intensity.append(round(sub[i].mean(),1))
print mean_intensity


# In[37]:

mean_intensity = []
for i in range(len(sub)):
    mi = round(sub[i].mean(),1)
    print (i+1), ":", mi
    mean_intensity.append(mi)


# In[38]:

# for odd-even parking pattern only
x = np.array(np.arange(100))
odds = x[1:100:2]
print odds
evens=x[0:100:2]
print evens


# In[39]:

# for odd-even parking pattern only
meanslice1 = []
for i in odds: 
    meanslice1.append(mean_intensity[i])
print meanslice1

meanslice2 = []
for i in evens: 
    meanslice2.append(mean_intensity[i])
print meanslice2
print max(meanslice1)
print min(meanslice2)


# In[40]:

thresh = 25
occupied = []  # the indexes start from 1
free = []
for i in range(len(sub)):
    if (sub[i].mean() > thresh):
        occupied.append(i+1)
    else:
        free.append(i+1)
print "occupied (", len(occupied), ") : ", occupied
print "free(", len(free), ") : ", free


# In[41]:

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


# In[42]:

img = Image.open(pic2_name)
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("FreeSansBold.ttf", 16)

xoffset = 10
yoffset = 10
index = 1  # note that the free index starts from 1
for row in range(10):
    for col in range(10):
        if(index in free):
            x = width*col + xoffset
            y = height*row + yoffset
            draw.text((x,y),"FREE",(255,0,100),font=font)
        index += 1
plt.imshow(img)
plt.show()     
fname = "out_"+pic2_name
img.save(fname)


# In[ ]:



