from airflow import DAG
from airflow.operators.bash import BashOperator

from group.group_download import downloads, transforms

from datetime import datetime
from airflow.utils.helpers import chain

with DAG('group_dag', start_date=datetime(2023, 1, 1), 
    schedule_interval=None, catchup=False) as dag:
 
    dl = downloads()

    ch  = BashOperator(
        task_id='check_files',
        bash_command='sleep 10'
    )

    tf = transforms()

chain(dl , ch , tf)