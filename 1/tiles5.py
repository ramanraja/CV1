# Tile car images for simulation
# coding: utf-8

# In[23]:

get_ipython().system(u'cd')
from PIL import Image, ImageDraw
import numpy as np
import random
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[24]:

initialCreation = False  # turn it on the first time you create an empty canvas from scratch
prob = 0.5  # probability of a slot being occupied


# In[25]:

numCars = 15
spriteFiles = ['images/scar{0}.jpg'.format(i) for i in range(1,numCars+1)]
#print spriteFiles
wd = []
ht = []
for sprite in spriteFiles:
    img = Image.open(sprite)
    wd.append(img.size[0])
    ht.append(img.size[1])
spriteWidth = max(wd)    
spriteHeight = max(ht)
print spriteWidth, spriteHeight


# In[26]:

xmargin = 8
ymargin = 8
roadWidth = 180
roadHeight = 150

canvasw = 1500  # starting estimate, to be revised soon
canvash = 900
ncols = canvasw/spriteWidth
nrows = canvash/spriteHeight

slotWidth = spriteWidth + xmargin
slotHeight = spriteHeight + ymargin
canvasWidth = ncols*(xmargin+slotWidth) + roadWidth
canvasHeight = nrows*(ymargin+slotHeight) + roadHeight

bgndColor = (180,180,180,0)
print ncols, nrows
print xmargin, ymargin
print spriteWidth, spriteHeight
print slotWidth, slotHeight
print canvasWidth, canvasHeight
print roadWidth, roadHeight 


# In[27]:

if initialCreation:
    canvas = Image.new("RGBA", (canvasWidth, canvasHeight), bgndColor)
    imd = ImageDraw.Draw(canvas) 
    y = ymargin
    for row in range(nrows):
        x = xmargin
        for col in range(ncols):
            if((col != 0) & (col != ncols/2)):
                imd.line((x-5,y, x-5, y+spriteHeight*0.7), fill=(255,255,255), width=4) 
            x = x + slotWidth + xmargin
            if (col== ncols/2-1):
                x = x + roadWidth
        y = y + slotHeight + ymargin
        if row == nrows/2-1:
            y = y + roadHeight
    roadTop = (canvasHeight - roadHeight)/2
    roadBottom = roadTop + roadHeight
    roadLeft = (canvasWidth - roadWidth)/2
    roadRight = roadLeft + roadWidth
    imd.line((0,roadTop, canvasWidth,roadTop), fill=(255,255,0), width=4)
    imd.line((0,roadBottom, canvasWidth,roadBottom), fill=(255,255,0), width=4)
    imd.line((roadLeft,0, roadLeft,canvasHeight), fill=(255,255,0), width=4)
    imd.line((roadRight,0, roadRight,canvasHeight), fill=(255,255,0), width=4)
    imd.line((roadLeft,roadTop, roadRight,roadTop), fill=bgndColor, width=4)
    imd.line((roadLeft,roadBottom, roadRight,roadBottom), fill=bgndColor, width=4)
    imd.line((roadLeft,roadTop, roadLeft,roadBottom), fill=bgndColor, width=4)
    imd.line((roadRight,roadTop, roadRight,roadBottom), fill=bgndColor, width=4)
    print canvas.size            
    canvas.show()
    #canvas.save("background.jpg", "JPEG")


# In[36]:

if initialCreation==False:
    prob = 0
    canvas = Image.open("background.jpg")
    print canvas.size
    imd = ImageDraw.Draw(canvas) 
    y = ymargin
    for row in range(nrows):
        x = xmargin
        for col in range(ncols):
            if (random.random() > prob):
                index = random.choice(range(numCars))
                sprite = Image.open(spriteFiles[index])
                w = sprite.size[0]
                h = sprite.size[1]
                box = (x,y, x+w, y+h)
                canvas.paste(sprite, box) 
            x = x + slotWidth + xmargin
            if (col== ncols/2-1):
                x = x + roadWidth
        y = y + slotHeight + ymargin
        if row == nrows/2-1:
            y = y + roadHeight
    print canvas.size            
    canvas.show()


# In[37]:

outfile = "canvas_{0}.jpg".format(prob)
canvas.save(outfile, "JPEG")
outfile


# In[ ]:



