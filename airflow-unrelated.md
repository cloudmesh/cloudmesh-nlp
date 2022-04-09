## Apache Airflow

Apache airflow provides an open source workflow magenment program for ease of monitoring and scheduling data pipelines. Apache is fully programmed in python and offers a multiture of sub packages to manage data.

The install of Apache airflow is documented here:

Step 1: install the packages for Apache airflow.
```
pip install apache-airflow
```
Step 2: Intalize the database.
```
airflow initdb
```
Step 3: Create a webserver with the default port 8080.
```
airflow webserver -p 8080
```
Step 4: start the scheduler.
```
airflow scheduler
```
The apache-airflow PyPI is a basic command package that gets you started with everything you need to use apache-airflow.
However, below are some comprehensive sub-packages for other usable resources.

Subpackage commands for apache airflow:

| subpackage      |   command                            |
|:---------------:|:------------------------------------:|
| s3              | ip install apache-airflow[s3]        |
| gcp_api         | pip install apache-airflow[gcp_api]  |
| mysql	pip       | install apache-airflow[mysql]        |
| postgres        | pip install apache-airflow[postgres] |
| hdfs 	pip       | install apache-airflow[hdfs]         |
| slack	pip       | install apache-airflow[slack]        |
| hive	pip       | install apache-airflow[hive]         |
| password        | pip install apache-airflow[password] |
| rabbitmq        | pip install apache-airflow[rabbitmq] |


More information surrounding apache-workflow can be can be found at: https://hevodata.com/learn/airflow/#t42

## Application of using airflow for NLP. 

HOWEVER THIS I NOT YOUR TASK YOU TASK IS TO FIGURE HOW TO USE GOOGLE API AND NOT AIRFLOW API

THis is a complete wrong link and is jsut an example on how to use an unrelated tool to use NLP, so this needs to be removed

More information can be found at:
<https://airflow.apache.org/docs/apache-airflow-providers-google/stable/index.html>
