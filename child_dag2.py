# -*- coding: utf-8 -*-

"""Child dag for external task sensor test"""

from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from airflow.models import DAG

default_args = {
    'owner': 'DataFactory',
    'start_date': datetime(2020, 11, 6, 10),
    'description': "Child dag to test ExternalTaskSensor operator. \
        Waiting for parent dag success in order to be triggered"
}

with DAG(dag_id="child_dag2", default_args=default_args, 
         schedule_interval="@hourly", catchup=False) as dag:
    dag.doc_md = __doc__
    is_data_in_s3 = ExternalTaskSensor(
        task_id='is_data_in_s3',
        external_dag_id='parent_dag2',
        external_task_id='data_is_sensed_in_s3',
        execution_delta=timedelta(hours=1),
        #start_date=datetime(2020, 11, 3,13, 40),
        timeout=480
    )

    is_data_in_s3.doc_md = """\
        Waiting for check_data_in_s3 completion in parent_dag
        """

    run_ssis = DummyOperator(
        task_id='run_ssis',
        dag=dag,
    )

    is_data_in_s3 >> run_ssis
