import pandas as pd

def validate_data(file_path):
    df = pd.read_parquet(file_path)
    assert 'state' in df.columns, "Missing 'state' column"
    assert df['brewery_type'].notna().all(), "Missing brewery_type values"
    print("✅ Validação concluída com sucesso")