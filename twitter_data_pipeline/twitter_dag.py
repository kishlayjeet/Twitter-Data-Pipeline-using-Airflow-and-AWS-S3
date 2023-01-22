from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from twitter_etl import run_twitter_etl


# Set default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 11, 8),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'schedule_interval': '@weekly'
}

# Create the DAG instance
dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='Kishlay\'s ETL Code'
)

# Create the PythonOperator for running the ETL task
run_etl = PythonOperator(
    task_id='complete_twitter_etl',
    python_callable=run_twitter_etl,
    dag=dag
)

run_etl >> dag
