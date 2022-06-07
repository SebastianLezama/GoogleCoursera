import os
from urllib import response
import requests
import json

"""
Convert .txt files into dict; then make a http post
"""

url = 'https://www.google.com'
#data = {}
source_path = ''
# response = requests.get(url)
# response.raise_for_status()
# response = requests.post(url, json=data)

people = []


def writeToTxt():
    os.chdir(cwdir)
    with open('data_2022.json', 'w') as f:
        json.dump(people, f, indent=2)


cwdir = 'c:\\Users\\Sebastian Lezama\\GoogleCoursera\\IT Automation\\'

def readFromTxt(file, dir):
    os.chdir(dir)
    with open(file, 'r') as f:
        data = json.load(f)
    return data


def getDb(source):
    os.chdir(source)
    for i in os.listdir(source):
        #resp = requests.get(url)
        resp = requests.post(url, json=readFromTxt(i, source))
        print(resp.request.body)

        #print(requests.post(url, json=readFromTxt(i)))


def main():
    getDb(cwdir)


if __name__ == '__main__':
    main()