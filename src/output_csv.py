import pickle
from sklearn.manifold import TSNE

data = pickle.load(open( "../processed/courses.p", "rb" ))

print(data[0].keys())
