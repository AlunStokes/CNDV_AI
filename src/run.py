import pickle
import tensorflow as tf
import tensorflow_hub as hub


data = pickle.load(open( "../processed/courses.p", "rb" ))

desc = []
i = 0
while i < len(data):
    desc.append(data[i]['desc'])
    i += 1

module_url = "https://tfhub.dev/google/nnlm-en-dim128/2"
embed = hub.KerasLayer(module_url)
embeddings = embed(desc)

i = 0
while i < len(data):
    data[i]['embedding'] = embeddings[i]
    i += 1

pickle.dump(data, open( "../processed/courses.p", "wb" ))
