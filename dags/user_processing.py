from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
import json

with DAG (
    dag_id='user_processing',
    start_date= datetime(2023,1,1),
    schedule='@daily',
    catchup=False
) as dag:
    
    create_table= PostgresOperator(
        task_id = 'create_table',
        postgres_conn_id = 'postgres',
        sql = '''
            CREATE TABLE IF NOT EXISTS USERS (
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                country TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL
            );
        '''
    )

    is_api_available = HttpSensor(
        task_id = 'is_api_available',
        http_conn_id = 'user_api',
        endpoint= 'api/'
    )

    extract_user = SimpleHttpOperator(
        task_id = 'extract_user',
        method= 'GET',
        http_conn_id= 'user_api',
        endpoint= 'api/',
        response_filter= lambda response: json.loads(response.text),
        log_response= True
    )