# post json objects to server
import os
import requests


url_test = 'https://httpbin.org/post'
url = 'http://[linux-instance-external-IP]/fruits'
path = '~/supplier-data/descriptions'


# Reads file, reads lines and posts requests
def batch_db_to_web_service(source): 
    os.chdir(source)
    keys = ['name', 'weight', 'description', 'image_name']
    data = []
    for file in os.listdir(source):
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
        print("Status code: " + str(resp.status_code))
        print("Request body: " + str(resp.request.body))
        print('-' * 30)


def main():
    list = batch_db_to_web_service(path)
    post_request(url, list)


if __name__ == '__main__':
    main()
