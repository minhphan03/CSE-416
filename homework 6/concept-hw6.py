import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import csr_matrix
from sklearn.preprocessing import normalize
from sklearn.metrics import pairwise_distances

def assign_clusters(data, centroids):
    """
    Parameters:
      - data      - is an np.array of float values of length n.
      - centroids - is an np.array of float values of length k.

    Returns
      -  A np.array of length n where the ith index represents which centroid
         data[i] was assigned to. The assignments range between the values 0, ..., k-1.
    """
    distances = pairwise_distances(data, centroids)
    return np.argmin(distances, axis=1)

def revise_centroids(data, k, cluster_assignment):
    """
    Parameters:
      - data               - is an np.array of float values of length N.
      - k                  - number of centroids
      - cluster_assignment - np.array of length N where the ith index represents which
                             centroid data[i] was assigned to. The assignments range between the values 0, ..., k-1.

    Returns
      -  A np.array of length k for the new centroids.
    """
    # TODO
    new_centroids = []
    for i in range(k):
        # Select all data points that belong to cluster i. Fill in the blank (RHS only)
        member_data_points = data[cluster_assignment == i]

        # Compute the mean of the data points. Fill in the blank (RHS only)
        centroid = member_data_points.mean(axis=0)
        
        # Convert numpy.matrix type to numpy.ndarray type
        centroid = np.ravel(centroid)
        new_centroids.append(centroid)

    new_centroids = np.array(new_centroids)
    return new_centroids

def kmeans(data, k, initial_centroids, max_iter, record_heterogeneity=None, verbose=False):
    # Note you can set verbose = True to see the outputs from each iteration, but leave verbose = False for submission
    """
    This function runs k-means on given data and initial set of centroids.
    
    Parameters:  
      - data                 - is an np.array of float values of length N.
      - k                    - number of centroids
      - initial_centroids    - is an np.array of float values of length k.
      - max_iter             - maximum number of iterations to run the algorithm
      - record_heterogeneity - if provided an empty list, it will compute the heterogeneity 
                               at each iteration and append it to the list. 
                               Defaults to None and won't record heterogeneity.
      - verbose              - set to True to display progress. Defaults to False and won't 
                               display progress.

    Returns  
      - centroids - A np.array of length k for the centroids upon termination of the algorithm.
      - cluster_assignment - A np.array of length n where the ith index represents which 
                             centroid data[i] was assigned to. The assignments range between the 
                             values 0, ..., k-1 upon termination of the algorithm.
    """
    centroids = initial_centroids[:]
    prev_cluster_assignment = None
    
    for itr in range(max_iter):  
        # Print itereation number
        if verbose:
            print(itr)
        
        # 1. Make cluster assignments using nearest centroids
        cluster_assignment = assign_clusters(data, centroids)
        print(cluster_assignment)
            
        # 2. Compute a new centroid for each of the k clusters, averaging all data points assigned to that cluster.
        centroids = revise_centroids(data, k, cluster_assignment)
            
        # Check for convergence: if none of the assignments changed, stop
        if prev_cluster_assignment is not None and \
          (prev_cluster_assignment == cluster_assignment).all():
            break
        
        # Print number of new assignments 
        if prev_cluster_assignment is not None:
            num_changed = sum(abs(prev_cluster_assignment - cluster_assignment))
            if verbose:
                print(f'    {num_changed:5d} elements changed their cluster assignment.')  
        
        prev_cluster_assignment = cluster_assignment[:]
        
    return centroids, cluster_assignment

data = np.array([
    [-1.88, 2.05],
    [-0.71, 0.42],
    [2.41, -0.67],
    [1.85, -3.80],
    [-3.69, -1.33]
])

initial_centroids = np.array([
    [2, 2],
    [-2, -2]
])

centroid, cluster_assignment = kmeans(data, 2, initial_centroids, max_iter=40, verbose=True)
print(cluster_assignment)