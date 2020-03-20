from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np

f = open("3k1.json", "r")
content = f.readlines()
f.close()

l = []

for i in range(len(content)):
    k = content[i].split(",")
    l.append(k[3][7:])
    

vectorizer = TfidfVectorizer()
vectorizer.fit(l)
vector = vectorizer.transform([l[0]])

if len(vectorizer.idf_) % 2 == 1:
    a = vectorizer.idf_[:-1]
else:
    a = vectorizer.idf_
c = a.reshape((int(len(a)/2), 2))

kmeans = KMeans(n_clusters=3)
kmeans.fit(c)
r = kmeans.cluster_centers_
plt.scatter(c[:,0], c[:,1] , s=50, c='b')
plt.scatter(r[0][0], r[0][1], s=200, c='g', marker='s')
plt.scatter(r[1][0], r[1][1], s=200, c='r', marker='s')
plt.scatter(r[2][0], r[2][1], s=200, c='y', marker='s')
plt.show()
print(kmeans.cluster_centers_)
print ("total data:", len(l))

