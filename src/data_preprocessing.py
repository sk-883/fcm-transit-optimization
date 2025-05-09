import pandas as pd
import geopandas as gpd
from src.config import RAW_DIR, PROCESSED_DIR


def load_ridership():
    return pd.read_csv(RAW_DIR / 'ridership.csv', parse_dates=['timestamp'])


def load_gps():
    return gpd.read_file(RAW_DIR / 'stops.geojson')


def clean_ridership(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=['stop_id', 'boardings'])
    df = df[df['boardings'] >= 0]
    return df


def merge_data(ridership: pd.DataFrame, gps: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    merged = gps.merge(ridership, on='stop_id')
    merged = gpd.GeoDataFrame(merged, geometry='geometry')
    return merged


def save_processed(gdf: gpd.GeoDataFrame):
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    gdf.to_file(PROCESSED_DIR / 'transport_processed.geojson', driver='GeoJSON')

if __name__ == '__main__':
    df = load_ridership()
    df = clean_ridership(df)
    gdf = load_gps()
    merged = merge_data(df, gdf)
    save_processed(merged)