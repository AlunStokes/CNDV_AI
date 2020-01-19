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

def tSNE(emb):
    tsne = TSNE(n_components=2, verbose=1, perplexity=15, n_iter=500)
    tsne_results = tsne.fit_transform(emb)
    df_subset = {}
    a = tsne_results[:,0]
    b = tsne_results[:,1]
    plt.figure(figsize=(16,10))
    sns.scatterplot(
        x=a, y=b,
        palette=sns.color_palette("hls", 10),
        legend="full",
        alpha=0.3
    )
    plt.show()

def embPCA(emb):
    pca = PCA(n_components=3)
    pca_result = pca.fit_transform(emb)
    a = pca_result[:,0]
    b = pca_result[:,1]
    c = pca_result[:,2]
    print('Explained variation per principal component: {}'.format(pca.explained_variance_ratio_))

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
