import numpy as np

def df_to_matrix(feat_df):
    # select columns for clustering
    return feat_df[['x', 'y', 'boardings']].T.values