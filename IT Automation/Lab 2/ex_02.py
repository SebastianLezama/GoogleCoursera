#! /usr/bin/env python3

import os
import requests


url = 'http://34.72.43.48/feedback'
cwdir = '/data/feedback'

def post_request(url, dict):
    resp = requests.post(url, json=dict)
    print(resp.request.body)
    print("Status code: " + str(resp.status_code))
    print('-' * 30)


def main(source): 
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


if __name__ == '__main__':
    main(cwdir)
