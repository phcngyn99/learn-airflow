from airflow import DAG
from datetime import datetime

with DAG (
    dag_id='user_processing',
    start_date= datetime(2023,1,1),
    schedule='@daily',
    catchup=False
) as dag:
    pass