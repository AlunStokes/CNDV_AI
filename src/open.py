import csv
import pickle

from util import *

data = {}
data['title'] = []
data['desc'] = []
data['type'] = []
data['code'] = []
data['duration'] = []
data['link'] = []
data['topic'] = []
data['bus_line'] = []
data['provider'] = []
data['community'] = []
data['audience'] = []

with open('../data/catalogue.csv', 'r') as file:
    reader = csv.reader(file)
    i = 0
    for row in reader:
        if i > 0:
            if row[6] == '':
                continue
            data['title'].append(row[1])
            data['desc'].append(row[2])
            data['type'].append(row[4])
            data['link'].append(row[3])
            data['code'].append(row[0])
            data['duration'].append(row[9])
            data['topic'].append(row[10])
            data['bus_line'].append(row[12])
            data['provider'].append(row[14])
            data['community'].append(row[16])
            data['audience'].append(row[18])
        i += 1

i = 0
while i < len(data['topic']):
    a = data['topic'][i]
    data['topic'][i] = a.split(';')
    i += 1

i = 0
while i < len(data['community']):
    a = data['community'][i]
    data['community'][i] = a.split(';')
    i += 1

i = 0
while i < len(data['audience']):
    a = data['audience'][i]
    if a == '':
        data['audience'][i] = ['Anyone']
    else:
        data['audience'][i] = a.split(';')
    i += 1

data = field_first_to_row(data)

pickle.dump(data, open( "../processed/courses.p", "wb" ))
