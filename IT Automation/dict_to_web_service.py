import os
import requests
import json


""" Exercise N2
Convert .txt files into dict; then make a http post.
"""


def write_to_txt(l):
    os.chdir(path)
    with open('data_2022.json', 'w') as f:
        json.dump(l, f, indent=2)


def read_from_txt(file, dir):
    os.chdir(dir)
    with open(file, 'r') as f:
        data = json.load(f)
    return data


# Converts list of dict into json
def data_to_json(list): 
        post_json = json.dumps(list, indent=2)
        return post_json


url = 'https://httpbin.org/post'
path = 'c:\\Users\\Sebastian Lezama\\GoogleCoursera\\IT Automation\\Text_files\\'


# Reads file, reads lines and posts requests
def batch_db_to_web_service(source): 
    os.chdir(source)
    keys = ['title', 'name', 'date', 'feedback']
    for file in os.listdir(source):
        print("Filename: " + file)
        data_dict = {}
        with open(file, 'r') as f:
            lines = f.read().splitlines()
            for index in range(len(lines)):
                data_dict[keys[index]] = lines[index]
        post_request(url, data_dict)


def post_request(url, d): #
    resp = requests.post(url, json=d)
    print("Status code: " + str(resp.status_code))
    print("Request body: " + str(resp.request.body))
    print('-' * 30)


def main():
    batch_db_to_web_service(path)


if __name__ == '__main__':
    main()
