import os
import requests
import json

url = 'http://34.72.43.48/feedback'
cwdir = '/data/feedback'

def data_to_json(list):
    post_json = json.dumps(list, indent=2)
    return post_json


def post_request(url, d):
    resp = requests.post(url, json=d)
    print(resp.request.body)
    print(resp.status_code)
    print('-' * 20)


def main(source):
    os.chdir(source)
    keys = ['title', 'name', 'date', 'feedback']
    for file in os.listdir(source):
        print(file)
        data_dict = {}
        raw_feedback = []
        with open(file, 'r') as f:
            lines = f.read().splitlines()
            for i in lines:
                raw_feedback.append(i)
            for index in range(4):
                data_dict[keys[index]] = raw_feedback[index]
        data = data_to_json(data_dict)
        post_request(url, data)


if __name__ == '__main__':
    main(cwdir)

#! /usr/bin/env python3

import os
import requests
import json

url = "http://35.225.188.54/feedback/"
cwdir = "/data/feedback/"
list_all = []

def data_to_json(l):
    post_json = json.dumps(l, indent=2)
    return post_json


def post_request(url, d):
    resp = requests.post(url, json=d)
    resp.raise_for_status()
    print(resp.request.body)
    print(resp.status_code)
    print('-' * 20)


def main(source):
    os.chdir(source)
    keys = ["title", "name", "date", "feedback"]
    for file in os.listdir(source):
        print(file)
        data_dict = {}
        raw_feedback = []
        with open(file, 'r') as f:
            lines = f.read().splitlines()
            for i in lines:
                raw_feedback.append(i)
            for index in range(4):
                data_dict[keys[index]] = raw_feedback[index]
        list_all.append(data_dict)
    data = data_to_json(data_dict)
    post_request(url, data)
#    post_request(url, list_all)


if __name__ == '__main__':
    main(cwdir)



