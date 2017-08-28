# using PIL (displays using the Windows image viewer)

import PIL
from PIL import Image

img = Image.open('bm.jpg')
img.show()  # opens the Windows default image viewer


