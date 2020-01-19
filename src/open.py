import csv
import pickle
import nltk
from nltk.corpus import stopwords as stop_words
import tensorflow as tf
import tensorflow_hub as hub

from utils import *

def list_to_sentence(l):
    s = ""
    l = [i.lower() for i in l]
    for i in l:
        s += i + " "
    return s[0:-1]

data = {}
data['title'] = []
data['desc'] = []
data['desc_clean'] = []
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
            s = list_to_sentence([w for w in row[2].split(' ') if not w in stop_words.words('english')] )
            data['desc_clean'].append(s)
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

titles = []
desc = []
i = 0
while i < len(data):
    titles.append(data[i]['title'])
    desc.append(data[i]['desc_clean'])
    i += 1

module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
embed = hub.KerasLayer(module_url)
embeddings_desc = embed(desc)
embeddings_titles = embed(titles)

i = 0
while i < len(data):
    data[i]['embedding_desc'] = embeddings_desc[i]
    data[i]['embedding_title'] = embeddings_titles[i]
    i += 1

pickle.dump(data, open( "../processed/courses.p", "wb" ))
