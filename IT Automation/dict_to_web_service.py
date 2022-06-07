import os
import requests
import json


""" Exercise N2
Convert .txt files into dict; then make a http post.
"""


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


# Reads file and appends dict into list
def batch_db_to_web_service(source): 
    os.chdir(source)
    keys = ['title', 'name', 'date', 'feedback']
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
        data = data_to_json(data_dict)
        post_request(url, data)


# Converts list of dict into json
def data_to_json(list): 
        post_json = json.dumps(list, indent=2)
        return post_json


def post_request(url, d): #
    resp = requests.post(url, data=d)
    print(resp.status_code)
    print(resp.request.body)


def main():
    batch_db_to_web_service(cwdir)



if __name__ == '__main__':
    main()
