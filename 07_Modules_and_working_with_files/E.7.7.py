
import os
import datetime


os.chdir(r'C:\Users\silvo\Desktop')
os.mkdir('New_folder')
my_directory = 'New_folder'
os.chdir(my_directory)

print('Current directory: ', os.getcwd())

current_date = datetime.datetime.now()

with open('example_file.txt', 'w') as file:
    file.write(str(current_date))

with open('example_file.txt', 'r') as file:
    print('File contents: ', file.read())
    print('Size in bytes: ', os.stat('example_file.txt').st_size)
    print('Time of creation: ', os.stat("example_file.txt").st_ctime)

