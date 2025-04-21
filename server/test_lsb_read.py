from PIL import Image
import numpy as np

image_path = "server/modified_boris.jpg"

with Image.open(image_path) as img:
    width,height = img.size
    data = np.array(img)

# flatten data
data = np.reshape(data, width*height*3)

# collects last bit
data = data & 1

data = np.packbits(data)

#contenrts intreger to unicode
for x in data:
    l = chr(x)
    if not l.isprintable():
        break
    print(l, end='')