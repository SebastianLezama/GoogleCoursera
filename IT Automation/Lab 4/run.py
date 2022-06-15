# post json objects to server
import os
import requests


url = 'https://httpbin.org/post'
path = 'c:\\Users\\Sebastian Lezama\\GoogleCoursera\\IT Automation\\Text_files\\'


# Reads file, reads lines and posts requests
def batch_db_to_web_service(source): 
    os.chdir(source)
    keys = ['name', 'weight', 'description', 'image_name']
    for file in os.listdir(source):
        print("Filename: " + file)
        data_dict = {}
        with open(file, 'r') as f:
            lines = f.read().splitlines()
            for index in range(len(lines)):
                if index == 1:
                    data_dict[keys[index]] = int(lines[index].strip('lbs'))
                    continue
                data_dict[keys[index]] = lines[index]
            data_dict[keys[3]] = str(os.path.splitext(file)[0]) + ".jpeg"
    return data_dict


def post_request(url, dict): #
    resp = requests.post(url, json=dict)
    print("Status code: " + str(resp.status_code))
    print("Request body: " + str(resp.request.body))
    print('-' * 30)


def main():
    dict = batch_db_to_web_service(path)
    post_request(url, dict)


if __name__ == '__main__':
    main()