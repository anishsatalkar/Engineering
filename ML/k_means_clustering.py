from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

points = [[0.1, 0.6], [0.15, 0.71], [0.08, 0.9],
          [0.16, 0.85], [0.2, 0.3], [0.25, 0.5],
          [0.24, 0.1], [0.3, 0.2]]

X = np.array(points)

init_clusters = np.ndarray(shape=(2, 2), dtype=float, buffer=np.array([points[0], points[7]]))

kmeans = KMeans(init=init_clusters, n_clusters=2, random_state=0).fit(X)

i = 1
m1_count = 0
m2_count = 0

for point, cluster_id in zip(points, kmeans.labels_):
    group = 'm' + str(cluster_id + 1)
    if cluster_id == 0:
        m1_count += 1
    else:
        m2_count += 1
    print('Point P{} belongs to : {}'.format(i, group))
    i += 1



print('Population of m1 : {} , Population of m2 : {}'.format(m1_count, m2_count))

print('Updated values of m1 : {} , m2 : {}'.format(kmeans.cluster_centers_[0], kmeans.cluster_centers_[1]))

x = []
y = []
for point in points:
    x.append(point[0])
    y.append(point[1])
plt.scatter(x,y,c=kmeans.labels_.astype(float))
plt.show()