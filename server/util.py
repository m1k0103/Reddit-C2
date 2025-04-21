import requests
import base64
#import piexif
#from PIL import Image
from exif import Image

# the bio will contain the 
def change_bio():
    pass


def hide_text(text):
    with open("server/boris.jpg", "rb") as f:
        img = Image(f.read())
        print(img)
        img.image_description = text

    with open("server/modified_boris.jpg", "wb") as new_f:
        new_f.write(img.get_file())
    
    print(dir(img))
    print("hidden text successfully")


def read_text(path):
    with open(path, "rb") as f:
        img = Image(f.read())
        try:
            secret = img.image_description
            print(secret)
        except KeyError:
            print(f"no secret found in {path}")


path = "server/modified_boris.jpg"
hide_text("hello world")
read_text(path)