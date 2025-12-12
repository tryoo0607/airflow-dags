from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timezone

with DAG(
        dag_id="hello_subdir_dag",
        start_date=datetime(2025, 12, 11, tzinfo=timezone.utc),
        schedule=None,
        catchup=False,
) as dag:
    EmptyOperator(task_id="start")
