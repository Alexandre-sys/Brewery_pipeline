import pandas as pd

def load_aggregated_data():
    df = pd.read_parquet("data/silver/breweries.parquet")
    agg_df = df.groupby(['brewery_type', 'state']).size().reset_index(name='count')
    agg_df.to_parquet("data/gold/breweries_aggregated.parquet", index=False)