from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Default DAG arguments
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Define the DAG
with DAG(
    dag_id='first_dag',
    default_args=default_args,
    description='My First DAG with Two Tasks',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False
) as dag:

    # First Task
    def greet():
        print("Hello, Apache Airflow!")

    task_1 = PythonOperator(
        task_id='greet_task',
        python_callable=greet
    )

    # Second Task
    def goodbye():
        print("Goodbye from Airflow!")

    task_2 = PythonOperator(
        task_id='goodbye_task',
        python_callable=goodbye
    )

    # Setting dependencies (task_2 runs after task_1)
    task_1 >> task_2
