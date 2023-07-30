from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.dates import days_ago
import os

from src import App
from src.configs.app import AppConfigs 
from src.configs.airflow import AirflowConfigs

def get_etl_file_names():
    return [
        file_name 
        for file_name in os.listdir(AppConfigs.DATA_FOLDER)
        if file_name.endswith('.csv')
    ]

dag = DAG(
    AppConfigs.NAME,
    default_args=AirflowConfigs.default_args,
    description=AppConfigs.DESCRIPTION,
    schedule_interval=AppConfigs.SCHEDULE_INTERVAL,
    start_date=days_ago(0, minute=1),
    catchup=False,
)

start = EmptyOperator(task_id="start")
finish = EmptyOperator(task_id="finish")
     
tasks = []
for file_name in get_etl_file_names():
    file_path = f'{AppConfigs.DATA_FOLDER}/{file_name}'
    current_task = PythonOperator(
        task_id=f'{file_name}',
        python_callable=App.run,
        op_kwargs={'file_paths': [file_path]},
        dag=dag,
    )
    tasks.append(current_task)
    
start >> tasks >> finish