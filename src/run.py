import pickle

data = pickle.load(open( "../processed/courses.p", "rb" ))

print(len(data))
