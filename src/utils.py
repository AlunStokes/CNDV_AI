import tensorflow as tf

from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import seaborn as sns
import csv

def field_first_to_row(d):
    l = []
    k = d.keys()
    i = 0
    while i < len(d[k[0]]):
        dn = {}
        for j in k:
            dn[j] = d[j][i]
        l.append(dn)
        i += 1
    return l

def row_to_field_first(d):
    pass

def find_by_field(d, f, v):
    l = []
    i = 0
    while i < len(d):
        if v in d[i][f]:
            l.append(d[i])
        i += 1
    return l

def export_tsv(emb, labels, file_name):
    s = ""
    for i in emb:
        for j in i:
            n = str(j.numpy())
            if 'e' in n:
                s += str(0)
            else:
                s += n
            s += '\t'
        s = s[0:-2]
        s += '\n'
    f = open('../processed/{}.tsv'.format(file_name),'w')
    f.write(s)
    f.close()

    s = ""
    for i in labels:
        s += i
        s += '\n'
    f = open('../processed/{}_meta.tsv'.format(file_name),'w')
    f.write(s)
    f.close()

def find_closest_n_points(d, data, n):
    p = d
    points = []
    i = 0
    while i < len(data):
        points.append(data[i]['embedding_desc'].numpy())
        i += 1
    dist = []
    for point in points:
        dist.append(np.linalg.norm(p - point))

    sm_index = find_smallest_n(dist, n)

    f = []
    for i in sm_index:
        f.append(data[i])
    return f

#Resturns indices
def find_smallest_n(l, n):
    a = []
    b = []
    while len(a) < n:
        i = 0
        sm = np.max(100)
        sm_i = 0
        while i < len(l):
            if len(a) == 0:
                if l[i] < sm and l[i] > 0:
                    sm = l[i]
                    sm_i = i
            else:
                if l[i] > np.max(a):
                    if l[i] < sm and l[i] > 0:
                        sm = l[i]
                        sm_i = i
            i += 1
        a.append(sm)
        b.append(sm_i)
    return b
