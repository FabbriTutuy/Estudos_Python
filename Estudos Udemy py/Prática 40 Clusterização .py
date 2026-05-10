import sklearn as sk
import matplotlib.pyplot as plt

x, y = sk.datasets.make_blobs(n_samples=500, centers=4, cluster_std=0.60, random_state=0)

plt.scatter(x[:, 0], x[:, 1], s=30)
plt.show()

clusters = 4
knmeas = sk.cluster.KMeans(n_clusters=clusters, random_state=0)
knmeas.fit(x)

predict = knmeas.predict(x)

plt.scatter(x[:, 0], x[:, 1], c=predict, s=30)

centroids = knmeas.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, alpha=0.75, label='Centroids')
plt.title('K-Means Clustering')
plt.legend()
plt.show()