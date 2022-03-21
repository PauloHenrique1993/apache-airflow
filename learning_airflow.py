from urllib import response
from itsdangerous import json
from learning_airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
import pandas as pd
import requests
import json

def captura_conta_dados():
    url = "https://data.cityofnewyork.us/resource/rc75-m7u3.json"
    response = requests.get(url)
    df = pd.DataFrame(json.loads(response.content))
    return len(df.index)

def e_valido(ti):
    qtd = ti.scom_pull(task_id='captura_conta_dados')
    if (qtd > 1000):
        return 'valido'
    return 'nvalido'

with DAG('learning_airflow',  start_date = datetime(2022,3,21),
            schedule_interval = '30 * * * *', catchup = False) as dag:
    
    captura_conta_dados = PythonOperator(
        task_id = 'captura_conta_dados',
        python_callable = 'captura_conta_dados'
    )

    e_valido = BranchPythonOperator(
        task_id = 'e_valido',
        python_callable = 'e_valido'
    )

    valido =  BashOperator(
        task_id = 'valido',
        bash_command = "echo 'Quantidade OK'"
    )

    nvalido =  BashOperator(
        task_id = 'nvalido',
        bash_command = "echo 'Quantidade NOK'"
    )