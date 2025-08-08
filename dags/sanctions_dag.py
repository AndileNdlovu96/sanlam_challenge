from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import subprocess

# Default DAG configuration
default_args = {
    'owner': 'sanlam',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

# Python function to run ingest script
def ingest():
    subprocess.run(["python3", "scripts/ingest.py"])

# Python function to run process script
def process():
    subprocess.run(["python3", "scripts/process.py"])

# Define DAG
with DAG('sanctions_batch_pipeline',
         schedule_interval='@daily',
         default_args=default_args,
         catchup=False) as dag:

    # Task 1: Ingest data
    ingest_task = PythonOperator(
        task_id='ingest_data',
        python_callable=ingest
    )

    # Task 2: Process data
    process_task = PythonOperator(
        task_id='process_data',
        python_callable=process
    )

    # Set task dependency
    ingest_task >> process_task
