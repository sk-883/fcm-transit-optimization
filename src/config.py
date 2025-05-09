from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / 'data' / 'raw'
PROCESSED_DIR = BASE_DIR / 'data' / 'processed'

# Clustering parameters
FCM_PARAMS = {
    'n_clusters': 5,
    'm': 2.0,
    'error': 1e-5,
    'maxiter': 1000
}