import os
import datetime

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

file_text = ("Sabrina Green,802-867-5309,System Administrator\n" + 
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

