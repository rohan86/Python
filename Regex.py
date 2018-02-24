import os
import re

path = r'/Users/Shona/Downloads'
filename='test1.txt'

file= os.path.join(path, filename)

print(file)


serchRegExSec = re.compile(r'^\s*\[\s*(.+?)\s*\]')
searchRegExVal = re.compile(r'^\s*(.+?)\s*=(.+?)\s*$')

for i in open(file, 'r'):
        match = serchRegExSec.search(i)
        if match:
            print('Found a section :{}'.format(match.group(1)))
        match = searchRegExVal.search(i)
        if match:
            print('Found value1 :{}'.format(match.group(1)))
            print('Found value2 :{}'.format(match.group(2)))
        else: print('Nothing found in : {}'.format(i))



