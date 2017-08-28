
# coding: utf-8

# In[61]:

get_ipython().system(u'cd')
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import numpy as np
import matplotlib.pyplot as plt
#% matplotlib inline


# In[75]:

pic2_name = 'canvas_0.2.jpg'
pic1 = Image.open('background.jpg')
print type(pic1)
print pic1.size  # width, height
pic2 = Image.open(pic2_name)
print pic2.size
#pic2.show()


# In[76]:

print pic1.size
print pic2.size
#pic1.size - pic2.size  # error
np.subtract(pic1.size, pic2.size)

# if background and foreground are of different sizes, do NOT crop them; panic !
if (pic1.size != pic2.size):
    print "PANIC: picture sizes are not the same !"


# In[77]:

# TODO: read these from config file
ncols, nrows = 14,4
xmargin, ymargin = 8,8
canvasWidth, canvasHeight = pic1.size[0], pic1.size[1]
slotWidth, slotHeight = 111, 195
roadWidth, roadHeight = 180, 150

print ncols, nrows
print canvasWidth, canvasHeight
print slotWidth, slotHeight
print roadWidth, roadHeight 


# In[78]:

spriteWindows = []
y = ymargin
for row in range(nrows):
    x = xmargin
    for col in range(ncols):
        spriteWindows.append([x,y,x+slotWidth, y+slotHeight])
        x = x + slotWidth + xmargin
        if (col== ncols/2-1):
            x = x + roadWidth
    y = y + slotHeight + ymargin
    if row == nrows/2-1:
        y = y + roadHeight
print spriteWindows        


# In[79]:

bgndSizes = []
for i in range(len(spriteWindows)):
    bgnd = pic1.crop(spriteWindows[i])
    file = "temp/bgnd%d.jpg"%i
    bgnd.save(file, "JPEG")
    s = os.path.getsize(file)
    bgndSizes.append(s)
print bgndSizes   


# In[80]:

fgndSizes = []
for i in range(len(spriteWindows)):
    fgnd = pic2.crop(spriteWindows[i])
    file = "temp/fgnd%d.jpg"%i
    fgnd.save(file, "JPEG")
    s = os.path.getsize(file)
    fgndSizes.append(s)
print fgndSizes     


# In[81]:

sizeDif = []
for i in range(len(spriteWindows)):
    sizeDif.append(fgndSizes[i]-bgndSizes[i]) 
print sizeDif

thresh = 500
occupied = []
free = []
for i in range(len(sizeDif)):
    if (sizeDif[i] > thresh):
        occupied.append(i)
    else:
        free.append(i)


# In[82]:

print "occupied: (", len(occupied), ")", occupied
print "free: (", len(free), ")", free
print ("----------------------------------------------------")


# In[83]:

print ("Camera ID      : 23")
print ("Level          : 4")
print ("Wing           : left")
print ("Zone           : AA")
print ("Total Capacity :"), len(spriteWindows)
print ("Occupied       :"), len(occupied)
print ("Free           :"), len(free)


# In[84]:

print free


# In[85]:

img = Image.open(pic2_name)
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("FreeSansBold.ttf", 16)


# In[86]:

xoffset = 10
yoffset = 10
index = 0  
for i in range(len(spriteWindows)):
    if(index in free):
        x = xoffset + spriteWindows[i][0]
        y = yoffset + spriteWindows[i][1]
        draw.text((x,y),"FREE",(0,0,0),font=font)
    index += 1
img.show()            


# In[87]:

fname = "out_"+pic2_name
img.save(fname)


# In[ ]:



