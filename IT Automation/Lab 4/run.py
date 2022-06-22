# post json objects to server
import os
import requests


url = 'http://35.225.80.22/fruits/'
path = 'supplier-data/descriptions/'


# Reads txt files, makes list of dicts.
def batch_db_to_list(source):
    keys = ['name', 'weight', 'description', 'image_name']
    data = []
    for file in os.listdir(source):
        if os.path.splitext(file)[1] != '.txt':
            continue
        data_dict = {}
        with open(source + file, 'r') as f:
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
    r_code = []
    for dict in list:
        resp = requests.post(url, data=dict)
        r_code.append(resp.status_code)
    return r_code


def main():
    list = batch_db_to_list(path)
    post_request(url, list)


if __name__ == '__main__':
    main()
