# post json objects to server
import os
import requests


url = 'http://[linux-instance-external-IP]/fruits'
path = '~/supplier-data/descriptions'


# Reads txt files, makes list of dicts.
def batch_db_to_list(source):
    os.chdir(source)
    keys = ['name', 'weight', 'description', 'image_name']
    data = []
    for file in os.listdir(source):
        if os.path.splitext(file)[1] != '.txt':
            continue
        data_dict = {}
        with open(file, 'r') as f:
            lines = f.read().splitlines()
            for index in range(len(lines)):
                if index == 1:
                    data_dict[keys[index]] = int(lines[index].strip('lbs'))
                    continue
                data_dict[keys[index]] = lines[index]
            data_dict[keys[3]] = str(os.path.splitext(file)[0]) + ".jpeg"
            data.append(data_dict)
    return data


def post_request(url, list):
    for dict in list:
        resp = requests.post(url, json=dict)
        return resp.status_code


def main():
    list = batch_db_to_list(path)
    post_request(url, list)


if __name__ == '__main__':
    main()
