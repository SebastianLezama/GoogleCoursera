# upload jpegs to server
import os
import requests


url = 'http://[linux-instance-IP-Address]/upload'
path = '~/supplier-data/images'

for image in os.listdir(path):
    if os.path.splitext(image)[1] == '.jpeg':
        with open(path + image, 'rb') as f:
            r = requests.post(url, files={'file': f})
