from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


def simple_function():
    print("Hello from the task execution")

# Dag with sequence operators for tasks
with DAG(
        dag_id="first_dag_with_python_and_bash",
        schedule=None,
        start_date=datetime(2024, 5, 17),  
        tags=['fousekis'] 
):
    empty_task = EmptyOperator(task_id="empty_task")
    simple_python_task = PythonOperator(task_id="simple_python_task", python_callable=simple_function)
    simple_bash_task = BashOperator(task_id="simple_bash_task", bash_command='echo "Hello from bash"')

    [empty_task, simple_python_task] >> simple_bash_task
