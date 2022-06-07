import os
import requests
import json

"""
Convert .txt files into dict; then make a http post
"""

#data = {}
# response = requests.get(url)
# response.raise_for_status()
# response = requests.post(url, json=data)


def write_to_txt(l):
    os.chdir(cwdir)
    with open('data_2022.json', 'w') as f:
        json.dump(l, f, indent=2)


def read_from_txt(file, dir):
    os.chdir(dir)
    with open(file, 'r') as f:
        data = json.load(f)
    return data


url = 'https://www.google.com'
cwdir = 'c:\\Users\\Sebastian Lezama\\GoogleCoursera\\IT Automation\\Text_files\\'
source_path = ''


def get_db(source): # Reads file and appends dict into list
    os.chdir(source)
    keys = ['title', 'name', 'date', 'feedback']
    list_of_dict = []
    for file in os.listdir(source):
        print(file)
        data_dict = {}
        raw_feedback = []
        with open(file, 'r', newline='') as f:
            lines = f.read().splitlines()
            for i in lines:
                raw_feedback.append(i)
            for index in range(len(raw_feedback)):
                data_dict[keys[index]] = raw_feedback[index]
            list_of_dict.append(data_dict)
    return list_of_dict


def get_post_json(list): # Converts list of dict into json
        post_json = json.dumps(list, indent=2)
        return post_json


def post_request(url, d):
    resp = requests.post(url, data=d)
    print(resp.status_code)
    print(resp.request.body)


def main():
    list = get_db(cwdir)
    data = get_post_json(list)
    post_request(url, data)


if __name__ == '__main__':
    main()
