from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt



def k_means_clustering(data, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    kmeans.fit(list(zip(range(len(data)), data)))
    plt.scatter(range(len(data)), data, c=kmeans.labels_)
    plt.show()

