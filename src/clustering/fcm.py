import numpy as np
from skfuzzy.cluster import cmeans

class FuzzyCMeans:
    def __init__(self, n_clusters=5, m=2.0, error=1e-5, maxiter=1000):
        self.n_clusters = n_clusters
        self.m = m
        self.error = error
        self.maxiter = maxiter
        self.centers = None
        self.u = None

    def fit(self, X: np.ndarray):
        # X: features shape (n_features, n_samples)
        cntr, u, _, _, _, _, _ = cmeans(
            data=X,
            c=self.n_clusters,
            m=self.m,
            error=self.error,
            maxiter=self.maxiter,
            init=None)
        self.centers = cntr
        self.u = u
        return cntr, u

    def predict(self, X: np.ndarray):
        # membership for new data
        _, u, _, _, _, _, _ = cmeans_predict(
            X, self.centers, self.m, error=self.error, maxiter=self.maxiter)
        return u.argmax(axis=0)