"""
import os
import datetime
import re 

# Unaware

def file_date(filename):
  # Create the file in the current directory
  with open(filename, 'w'):
    pass
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  time = str(datetime.datetime.fromtimestamp(timestamp))
  # Return just the date portion Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(time[:10]))
# print(file_date("newfile.txt")) Should be today's date in the format of yyyy-mm-dd

def parent_directory(relative_parent):
  # Create a relative path to the parent of the current working directory 
  relative_parent = os.path.join(os.getcwd(), '..')

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

def script(filename):
    comments = '# help'
    with open(filename, 'w') as file:
        file.write(comments)
    filesize = os.path.getsize(filename)
    return filesize


print(script('Program.py'))
os.remove('Program.py')

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open(filename, 'w') as file:
    pass

  # Return the list of files in the new directory
  return os.listdir('./')

print(new_directory("PythonPrograms", "script.py"))

os.remove('script.py')
os.chdir('../')
os.chdir('GoogleCoursera')
# print(os.getcwd())
# os.remove(parent_directory('PythonPrograms'))

import csv

file_text = (
  "Sabrina Green,802-867-5309,System Administrator\n" + 
  "Eli Jones,683-348-1127,IT Specialist\n" +
  "Melody Daniels,846-687-7436,Programmer\n" +
  "Charlie Rivera,698-746-3357,Web Developer"
)
with open('csv_file.txt', 'w') as file:
  file.write(file_text)
f = open("csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f:
  name, phone, role = row
  print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
f.close()

# Write to csv with the csv.writer funtion
# You can use csv.DictWriter to write from a dict with keys and asign them to the key values
# Writing with the writeheader() function

file_data = [['name', 'phone', 'role'],
  ['Sabrina Green', '802-867-5309', 'System Administrator'],
  ['Eli Jones', '683-348-1127', 'IT Specialist'],
  ['Melody Daniels', '846-687-7436', 'Programmer'],
  ['Charlie Rivera', '698-746-3357', 'Web Developer']
  ]

with open('csv_file.txt', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerows(file_data)
with open('csv_file.txt') as file:
  reader = csv.DictReader(file)
  for row in reader:
    print("Name: {}, Phone: {}, Role: {}".format(row['name'], row['phone'], row['role']))

# Regular Expressions
# .^$?*[] special characters. \ escape character
# . Any character
# ^ Beginning of a line, $ end of a line
# + Matches one or more occurrences of the character that comes before it
# \w matches letters, numbers and underscores
# ? goes before expression, optional
# () capturing groups, can be indexed, i[0] is the whole tuple then +=
# \b boundary, match lenght of expression; {n} numerical repetition can be a range

import re

def repeating_letter_a(text):
  result = re.search(r"[aA].*[aA]", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False

reg = (r"[\w*][\s*]\w*")

# it starts with an uppercase letter, followed by
# at least some lowercase letters or a space, and ends with
#  a period, question mark, or exclamation point.
#result = re.search(r"^[A-Z][a-z ]*[\.\?!]$")

pattern = r"^[a-zA-Z][a-zA-Z\.-+_]*[\..]$"

# subprocess module
import subprocess

result = subprocess.run(["host", "8,8,8,8"], capture_output=True)
print(result.returncode)
print(result.stdout.decode().split()) # decodes the stdout with u8

# prepare new env and set path var

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env['PATH']])

result = subprocess.run(["myapp"], env=my_env)
print(result[1])

# Handling log file, for line in to avoid RAM buildup
import sys

logfile = sys.argv[1]
usernames = {}
# checks for users to started a CRON job
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    pattern = r"USER \((\w+)\)$"
    result = re.search(pattern, line)
    if result is None:
      continue
    name = result[1]
    usernames[name] = usernames.get(name, 0) + 1
print(usernames)


def show_time_of_pid(line):
  pattern = (r"^([A-Z][a-z]* \d{,2} \d*:\d{2}:\d{2})[\w.+-= ]*\[(\d*)\]")
  result = re.search(pattern, line)
  if result == None:
    return ''
  return result[1] + " pid:" + result[2]

# Dict to count appearences of strings

usernames = {}
name = "user"
usernames[name] = usernames.get(name, 0) + 1

import json


def convertToJson(people): # Converts list of dict into json
  with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)

def loadFromJson():
  with open('people_json', 'r') as people_json:
    people = json.load(people_json)


import yaml

def convertToYaml(people): # Converts list of dict into YAML
  with open('people.yaml', 'w') as people_yaml:
    yaml.safe_dump(people, people_yaml)


import requests


url = 'https://www.google.com'
response = requests.get(url)
response.ok # True
response.status_code # 200

if not response.ok:
  raise Exception("GET failed with status code {}".format(response.status_code))
response.raise_for_status() # Raises an HTTPError if response not ok

par = {"search": "grey kitten", "max_results": 15}
res = requests.get(url, params=par) # ?search=grey+kitten&max_results=15
print(response.request.url)

p = {"descripion": "white kitten", "name": "Snowball", "age_months": 6}
response = requests.post(url, data=p)
print(response.request.body) # 'description=white+kitten&name=Snowball&age_months=6'
response = requests.post(url, json=p) # Sends data from dict as JSON
"""

import os
from email.message import EmailMessage

print(os.getcwd())
os.chdir('GoogleCoursera')
print(os.getcwd())

message = EmailMessage()
sender = "me@example.com"
recipient = "you@example.com"
message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greeting from {} to {}.'.format(sender, recipient)
body = """Hey there,

I'm learning Python!"""
message.set_content(body)

import os.path
import mimetypes

attachment_path = './report.pdf' # example.png
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path) # image/png -> type/subtype
mime_type, mime_subtype = mime_type.split('/', 1) # image png

with open(attachment_path, 'rb') as ap:
  message.add_attachment(ap.read(), 
                        maintype=mime_type,
                        subtype=mime_subtype,
                        filename=attachment_filename)

print(message)

import smtplib

mail_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
port = 465
# another_mail_server = smtplib.SMTP_SSL('smtp.example.com')
# another_mail_server.set_debuglevel(1) # can set both to see smtp msgs being sent

import getpass

mail_pass = getpass.getpass('Password?') # gets pass from input
mail_server.login(sender, mail_pass) # returns tuple of status, u need to handle smtp auth error exception
mail_server.send_message(message) # returns dict of unreached receipients
mail_server.quit()

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie


fruit = {
  "apples" : 8,
  "bananas" : 6,
  "cherries" : 12,
  "oranges" : 6
}


report = SimpleDocTemplate('./report.pdf')
styles = getSampleStyleSheet()
report_title = Paragraph("A Complete Inventory of My Fruit", styles['h1'])
table_data = []
for k, v in fruit.items():
  table_data.append([k, v])

table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign='LEFT')

report_pie = Pie(width=3, height=3)
report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
  report_pie.data.append(fruit[fruit_name])
  report_pie.labels.append(fruit_name)

report_chart = Drawing()
report_chart.add(report_pie)

report.build([report_title, report_table, report_chart])

