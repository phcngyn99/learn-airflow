from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup

def downloads():
    with TaskGroup(group_id= "download", tooltip= "Downloads") as group:
        download_a = BashOperator(
            task_id='download_a',
            bash_command='sleep 10'
        )

        download_b = BashOperator(
            task_id='download_b',
            bash_command='sleep 10'
        )

        download_c = BashOperator(
            task_id='download_c',
            bash_command='sleep 10'
        )
    return group

def transforms():
    with TaskGroup("transform") as gr:
         
        transform_a = BashOperator(
            task_id='transform_a',
            bash_command='sleep 10'
        )
    
        transform_b = BashOperator(
            task_id='transform_b',
            bash_command='sleep 10'
        )
    
        transform_c = BashOperator(
            task_id='transform_c',
            bash_command='sleep 10'
        )
    return gr
