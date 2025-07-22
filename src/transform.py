import pandas as pd
import os

def transform_brewery_data(file_path):
    df = pd.read_json(file_path)
    df.drop_duplicates(inplace=True)
    df = df[df['state'].notna()]
    os.makedirs("data/silver", exist_ok=True)
    df.to_parquet("data/silver/breweries.parquet", partition_cols=['state'])