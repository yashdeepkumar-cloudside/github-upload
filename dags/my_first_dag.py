from datetime import timedelta

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_ards = {
	'owner': 'airflow',
	'start_date':datetime(2023, 9, 12)
	'end_date': datetime(2023, 9, 12)
	'email': ['yashdeepkumar24@gmail.com'],
	'email_on_failure': False,
	'email_on_retry': False,
	'retries': 1,
	'retry_delay': timedelta(minutes=5),
}