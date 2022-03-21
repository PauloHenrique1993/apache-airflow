# apache-airflow

Instalando o apache airflow e agendando um pequeno schedule.

## Instalação

Criando o diretório onde ficara o projeto

$ mkdir apache-airflow

$ cd apache-airflow

$ python3 -m venv .venv

$ source .venv/bin/activate

Agora vamos instalar o airflow

$ pip install apache-airflow

Após a instalação, iremos definir uma variável de ambiente que indica onde o airflow está instalado. (caso tenha instalado em outro lugar é só passar o caminho)

$ export AIRFLOW_HOME=$PWD

Agora vamos inicializar o ambiente.

$ airflow db init

Agora vamos criar um usuário do airflow

$ airflow users create \\ </br>
    --username admin \\ </br>
    --firstname Paulo \\ </br>
    --lastname Henrique \\</br>
    --role Admin \\</br>
    --email seuemail@email.com
    
Após criar o usuário vamos subir o servidor. (Caso não seja passado a porta ele irá rodar por padrão na porta 8080).

$ airflow webserver -p 8084


