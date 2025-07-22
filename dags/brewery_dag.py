from airflow import DAG #ignorar 
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.extract import extract_brewery_data
from src.transform import transform_brewery_data
from src.load import load_aggregated_data
from src.validate import validate_data
import os

def get_latest_bronze_file():
    files = sorted(os.listdir("data/bronze"))
    return os.path.join("data/bronze", files[-1])

with DAG(
    dag_id="brewery_pipeline",
    start_date=datetime(2023,1,1),
    schedule="@daily",
    catchup=False) as dag:

    extract = PythonOperator(
        task_id="extract",
        python_callable=extract_brewery_data
    )

    transform = PythonOperator(
        task_id="transform",
        python_callable=lambda: transform_brewery_data(get_latest_bronze_file())
    )

    load = PythonOperator(
        task_id="load",
        python_callable=load_aggregated_data
    )

    validate = PythonOperator(
        task_id="validate",
        python_callable=lambda: validate_data("data/gold/breweries_aggregated.parquet")
    )

    extract >> transform >> load >> validate

#colocar pra salvar em delta também