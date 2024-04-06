import re

def createFilePattern(fileFormat):
    return fr'^[\d\w\s\.\-\+\_\(\)\[\]]+\.{fileFormat}$'

pdfPattern = createFilePattern('pdf')
pngPattern = createFilePattern('png')
jpgPattern = createFilePattern('jpg')


list = ['matheus.pdf', 'matheus.png', 'water.jpg']

pdfGroup = []

for item in list:
    if (re.match(pdfPattern, item)):
        pdfGroup.append(item)

print(pdfGroup)