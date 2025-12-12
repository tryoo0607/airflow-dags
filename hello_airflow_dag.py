from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
        dag_id="hello_airflow",
        start_date=datetime(2024, 1, 1),
        schedule=None,     # ⭐ Airflow 3 필수
        catchup=False,
        tags=["test"],
) as dag:

    hello = BashOperator(
        task_id="say_hello",
        bash_command="echo 'Hello Airflow 3'",
    )

    hello
