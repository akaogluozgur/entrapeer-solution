"""
DAG file for running the data extraction tasks with Airflow.

This DAG file defines the data extraction tasks using Airflow. It sets up a DAG with a start
and finish task, and creates PythonOperator tasks for each ETL file found in the data folder.
The ETL tasks are performed using the `App.run` method.

DAG Properties:
    Name: The name of the DAG.
    Default Args: Default arguments for the DAG.
    Description: A brief description of the DAG.
    Schedule Interval: The schedule interval for the DAG.
    Start Date: The start date for the DAG execution.

Tasks:
    start: An empty operator to indicate the start of the DAG.
    finish: An empty operator to indicate the finish of the DAG.
    tasks: PythonOperator tasks for each ETL file found in the data folder.
"""

import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.dates import days_ago

from src import App
from src.configs.app import AppConfigs
from src.configs.airflow import AirflowConfigs


def get_etl_file_names():
    """
    Get a list of ETL file names from the data folder.

    Returns:
        List[str]: A list of file names for ETL files found in the data folder.
    """
    return [
        data
        for data in os.listdir(AppConfigs.DATA_FOLDER)
        if data.endswith('.csv')
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

start >> tasks >> finish  # pylint: disable=pointless-statement
