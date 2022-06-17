# upload jpegs to server
import os
import requests


url = 'http://[linux-instance-IP-Address]/upload'
path = '~/supplier-data/images'

for image in os.listdir(path):
    with open(image, 'rb') as f:
        r = requests.post(url, files={'file': f})
