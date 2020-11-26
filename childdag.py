from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.sensors import ExternalTaskSensor

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 4, 29),
}

dag = DAG('Child_dag', default_args=default_args, schedule_interval='@daily')

# Use ExternalTaskSensor to listen to the Parent_dag and cook_dinner task
# when cook_dinner is finished, Child_dag will be triggered
wait_for_dinner = ExternalTaskSensor(
    task_id='wait_for_dinner',
    external_dag_id='Parent_dag',
    external_task_id='cook_dinner',
    start_date=datetime(2020, 4, 29),
    execution_delta=timedelta(hours=1),
    timeout=3600,
)

have_dinner = DummyOperator(
    task_id='have_dinner',
    dag=dag,
)
play_with_food = DummyOperator(
    task_id='play_with_food',
    dag=dag,
)

wait_for_dinner >> have_dinner
wait_for_dinner >> play_with_food
