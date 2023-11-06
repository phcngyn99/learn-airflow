from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
 
from datetime import datetime
 
def _t1(ti):
    ti.xcom_push(key = 'mkey', value = 2002)
 
def _t2(ti):
    holder = ti.xcom_pull(key = 'mkey', task_ids = 't1')
    print(f"THIS IS A FUCKING XCOM TEST: {holder}")
 
with DAG("xcom_dag", start_date=datetime(2023, 1, 1), 
    schedule_interval=None, catchup=False) as dag:
 
    t1 = PythonOperator(
        task_id='t1',
        python_callable=_t1
    )
 
    t2 = PythonOperator(
        task_id='t2',
        python_callable=_t2
    )
 
    t3 = BashOperator(
        task_id='t3',
        bash_command="echo ''"
    )
 
    t1 >> t2 >> t3