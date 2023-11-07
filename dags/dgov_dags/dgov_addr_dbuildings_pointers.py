import sys

import pendulum
from airflow.operators.python import PythonOperator
from airflow.models import DAG
from airflow.models import Variable

sys.path.append('.')

from dags.docker_runner import ExternalEtlDockerRunner as Runner
from dags.dgov_dags.common import get_dict_command_args

with DAG(
        dag_id='dgov_address_register_dbuildings_pointers',
        catchup=False,
        start_date=pendulum.now(tz=f'{Variable.get("TZ")}').subtract(days=1),
        schedule_interval='@monthly',
        tags=['dgov_address']
     ) as dag:

    command_args = PythonOperator(
        task_id='command_args',
        python_callable=get_dict_command_args,
        dag=dag,
        do_xcom_push=False,
    )

    dgov_address_register_dbuildings_pointers = Runner(
        task_id='dgov_address_register_dbuildings_pointers',
        luigi_module='dgov_addrreg',
        luigi_task='DgovAddrRegDBuildingsPointers',
        luigi_params="{{ task_instance.xcom_pull(task_ids='command_args', key='command_args') }}",
        env_vars={'DATAGOV_TOKEN': Variable.get('DATAGOV_TOKEN')},
        pool='dgov_address',
        do_xcom_push=False
    )

    command_args >> dgov_address_register_dbuildings_pointers
