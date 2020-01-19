import pickle

from utils import *

data = pickle.load(open( "../processed/courses.p", "rb" ))

emb = []
labels = []
i = 0
while i < len(data):
    emb.append(data[i]['embedding_desc'])
    labels.append(data[i]['title'])
    i += 1

export_tsv(emb, labels, 'emb_desc')
