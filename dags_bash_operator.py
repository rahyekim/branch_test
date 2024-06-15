import datetime
import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator",
    schedule=" 0 0 * * *",
    start_date=pendulum.datetime(2024,6,10, tz="Asia/Seoul"),
    catchup=False,
    tags=[testing],
) as dag:
    bash_t1=BashOperator(
        task_id="bash_t1",
        bach_command="echo whoami",
    )
    bash_t2=BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME"
    )
    bash_t1 >> bash_t2

    