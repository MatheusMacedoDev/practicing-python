import os
import re

filesList = []

filePattern = r'^[\d\w\s\.\-\+\_\(\)\[\]]+\.[0-9a-z]{2,5}$'

with os.scandir('C:/Users/mathe/Downloads') as entries:
    for entry in entries:
        if (re.match(filePattern, entry.name) != None):
            filesList.append(entry.name)
            print(entry.name)

print(len(filesList))