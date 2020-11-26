# -*- coding: utf-8 -*-

"""Parent dag for external task sensor test"""

from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.models import DAG


default_args = {
    'owner': 'DataFactory',
    'start_date': datetime(2020, 11, 6, 10),
    'description': "Parent dag to test ExternalTaskSensor operator. This dag will trigger the child dag on success"
}

with DAG(dag_id="parent_dag2", default_args=default_args,
         schedule_interval="@hourly", catchup=False) as dag:
    dag.doc_md = __doc__

    get_data = DummyOperator(
        task_id='get_data',
        dag=dag
    )

    data_is_sensed_in_s3 = BashOperator(
        task_id="data_is_sensed_in_s3",
        bash_command="echo 'command executed from BashOperator'")

    data_is_sensed_in_s3.doc_md = """\
        Check if if the file is in s3. If it's case, child dag is triggeerd
        """

    get_data >> data_is_sensed_in_s3
