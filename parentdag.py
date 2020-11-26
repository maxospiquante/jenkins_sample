from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 4, 29),
}

dag = DAG('Parent_dag', default_args=default_args, schedule_interval='@daily')

leave_work = DummyOperator(
    task_id='leave_work',
    dag=dag,
)
cook_dinner = DummyOperator(
    task_id='cook_dinner',
    dag=dag,
)

leave_work >> cook_dinner
