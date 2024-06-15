
my_dag=DAG(
    dag_id="dags",
    schedule=None,
    tags=[homework],
)

bash_t1=BashOperator(
        task_id="bash_t1",
        bash_Command="echo whoami"
        dag=my_dag)

bash_t1 >> bash_t2

왜 안되냐고