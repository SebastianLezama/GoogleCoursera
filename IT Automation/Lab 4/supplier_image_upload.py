# upload jpegs to server
import os
import requests


url = ''
path = ''

for image in os.listdir(path):
    with open(image, 'rb') as f:
        r = requests.post(url, files={'file': f})
