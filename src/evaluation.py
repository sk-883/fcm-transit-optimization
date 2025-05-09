import pandas as pd
import numpy as np
from sklearn.metrics import silhouette_score
from src.config import PROCESSED_DIR


def load_features():
    return pd.read_csv(PROCESSED_DIR / 'transport_features.csv')


def evaluate_clusters(X: np.ndarray, labels: np.ndarray):
    score = silhouette_score(X.T, labels)
    return {'silhouette': score}


def main():
    df = load_features()
    X = df[['x','y','boardings']].values
    labels = np.load(PROCESSED_DIR / 'labels.npy')
    metrics = evaluate_clusters(X, labels)
    print('Silhouette Score:', metrics['silhouette'])

if __name__ == '__main__':
    main()