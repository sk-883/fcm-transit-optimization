import pandas as pd
import geopandas as gpd
from src.config import PROCESSED_DIR


def aggregate_time_window(gdf: gpd.GeoDataFrame, freq: str = '1H') -> pd.DataFrame:
    df = pd.DataFrame(gdf.drop(columns='geometry'))
    df = df.set_index('timestamp')
    agg = df.groupby('stop_id').resample(freq)['boardings'].sum().reset_index()
    return agg


def assign_geofences(agg: pd.DataFrame) -> pd.DataFrame:
    # placeholder: for each stop, use its coordinates to assign to grid cells
    agg['x'] = agg['longitude']
    agg['y'] = agg['latitude']
    return agg


def main():
    gdf = gpd.read_file(PROCESSED_DIR / 'transport_processed.geojson')
    agg = aggregate_time_window(gdf)
    feat = assign_geofences(agg)
    feat.to_csv(PROCESSED_DIR / 'transport_features.csv', index=False)

if __name__ == '__main__':
    main()