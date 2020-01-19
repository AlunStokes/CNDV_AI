import pickle
import numpy as np
import matplotlib.pyplot as plt

def time_to_minutes(t):
    a = t.split(':')
    return int(a[0]) * 60 + int(a[1])

data = pickle.load(open( "../processed/courses.p", "rb" ))


topics = []
i = 0
while i < len(data):
    l = data[i]['type']
    if l not in topics:
        topics.append(l)
    i += 1

print(topics)
exit()

lengths = {}

for topic in topics:
    lengths[topic] = []

num = 0
for topic in topics:
    i = 0
    while i < len(data):
        if topic in data[i]['topic']:
            num += 1
            lengths[topic].append(time_to_minutes(data[i]['duration']))
        i += 1

for k in lengths.keys():
    lengths[k] = np.mean(lengths[k])

l = []
for k in lengths.keys():
    print("{}: {}".format(k, lengths[k]))
