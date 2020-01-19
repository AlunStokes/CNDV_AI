import pickle
import tensorflow as tf
import tensorflow_hub as hub

from utils import *


data = pickle.load(open( "../processed/courses.p", "rb" ))

'''emb = []
labels = []
i = 0
while i < len(data):
    emb.append(data[i]['embedding_desc'])
    labels.append(data[i]['title'])
    i += 1

export_tsv(emb, labels, 'emb_desc')'''

module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
embed = hub.KerasLayer(module_url)
embeddings_desc = embed(["This course seeks to inform students of the complexities associated with language aqusition, and strategies to aid ESL students with this skill."])

c = find_closest_n_points(embeddings_desc[0].numpy(), data, 5)

for i in c:
    print(i['title'])
