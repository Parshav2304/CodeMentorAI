from sklearn.cluster import KMeans

class WeaknessCluster:
    def __init__(self, k=3):
        self.model = KMeans(n_clusters=k, random_state=42)

    def fit(self, X):
        self.model.fit(X)

    def predict(self, X):
        return self.model.predict(X)
