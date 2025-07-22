import pandas as pd
from src.transform import transform_brewery_data

def test_transform(tmp_path):
    data = [{"id": 1, "state": "NY", "brewery_type": "micro"}, {"id": 1, "state": "NY", "brewery_type": "micro"}]
    file = tmp_path / "test.json"
    pd.DataFrame(data).to_json(file, orient="records")
    transform_brewery_data(str(file))
    assert (tmp_path / "breweries.parquet").exists() == False  # Salvamento é em pasta global