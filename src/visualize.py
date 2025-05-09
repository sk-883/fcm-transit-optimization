import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from src.config import PROCESSED_DIR


def plot_clusters():
    gdf = gpd.read_file(PROCESSED_DIR / 'transport_processed.geojson')
    df = pd.read_csv(PROCESSED_DIR / 'transport_features.csv')
    df['cluster'] = pd.read_csv(PROCESSED_DIR / 'labels.csv')['cluster']
    merged = gdf.merge(df, on=['stop_id','timestamp'])
    merged.plot(column='cluster', categorical=True, legend=True)
    plt.title('FCM Clusters of Stops')
    plt.show()

if __name__ == '__main__':
    plot_clusters()