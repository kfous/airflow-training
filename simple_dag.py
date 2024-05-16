from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
        dag_id="first_dag",
        schedule=None,
):
    empty_task = EmptyOperator(task_id="empty_task")
