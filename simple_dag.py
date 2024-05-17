from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="first_dag",
    schedule_interval=None,  
    start_date=datetime(2024, 5, 17),  
    tags=['fousekis']  
) as dag:
    empty_task = EmptyOperator(task_id="empty_task")