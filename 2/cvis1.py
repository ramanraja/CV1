# read and write images using PIL

from PIL import Image
im = Image.open('C:/Users/Raja/PythonWD/CV/image4/photo.png')
print im.size 
im2 = Image.new('RGBA', (20, 20))
im2.save('C:/Users/Raja/PythonWD/CV/image4/transparentImage.png')